from piece import Pawn, Rook, Knight, Bishop, Queen, King, Empty

class Board:
    def __init__(self):
        self.board = []
        self.turn = 'w'
        self.move_count = 1

    def loadFromFen(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        piece_type_from_symbol = {'k': King, 'q': Queen, 'r': Rook, 'b': Bishop, 'n': Knight, 'p': Pawn}
        
        fen_board = fen.split(' ')[0][::-1].split('/') # Isolate the part relating to board arrangement
        
        for rows in fen_board:
            for symbol in rows[::-1]: # Puts the FEN string in the correct order for indexing later
                if symbol.isdigit(): # Appends blank spaces to the board
                    for _ in range(int(symbol)):
                        self.board.append(Empty())
                else: # Appends pieces to the board
                    piece_colour = 'W' if symbol.isupper() else 'B' # Assings piece colour
                    piece_type = piece_type_from_symbol[symbol.lower()] # Assigns piece type
                    self.board.append(piece_type(piece_colour)) # Appends piece
        self.turn = fen.split(' ')[1] # Sets correct turn based on FEN string

    def printBoard(self):
        # from os import system, name
        # system('cls' if name == 'nt' else 'clear') # Clear the terminal output
        print(" +--+--+--+--+--+--+--+--+")
        row_num = 8
        for i in range(7, -1, -1): # Prints the board
            print(str(row_num)+"|", end="")
            for j in range(8):
                current = self.board[i*8 + j]
                try:
                    print(f"{current.getColour()}{current.getType()}|", end="")
                except AttributeError:
                    print("  |", end="")
            print("\n +--+--+--+--+--+--+--+--+")
            row_num -= 1
        print(f"  a  b  c  d  e  f  g  h\t{self.turn.upper()}'s turn")

    def move(self, start: tuple, end: tuple):
        working_index = start[0]*8 + start[1] # Puts the coordinate format into the correct format for indexing the array
        working = self.board[working_index]
        target_index = end[0]*8 + end[1]
        target = self.board[target_index]

        check =  working.isValid(working, target, working_index, target_index, self.turn, self.board) # Checks move validity
        print(check)
        
        if check: # Makes the move
            self.log(end, target)
            self.board[target_index] = working
            self.board[working_index] = Empty()
            self.turn = 'B' if self.turn == 'W' else 'W'
            self.move_count += 1 if self.turn == 'B' else 0
        else:
            print("Invalid move")

    def isWon(self):
        return False

    def log(self, end: tuple, target) -> None:
        # Write to a file in the format of PGN
        with open(r'/Users/edwardbaker/Documents/nea/chess/output/log.log', 'a+') as log:
            if self.turn == 'w':
                log.write(f"{self.move_count}. {target.getType() if target.getType() != 'P' else ''}{chr(end[1]+97)}{end[0]+1} ")
            else:
                log.write(f"{target.getType() if target.getType() != 'P' else ''}{chr(end[1]+97)}{end[0]+1}" + "\n")

if __name__ == '__main__':
    print("File run incorrectly - please run game.py instead")
