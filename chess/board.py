from piece import Pawn, Rook, Knight, Bishop, Queen, King, Empty

class Board:
    '''Class for the board'''
    def __init__(self):
        self.board = []
        self.turn = 'w'
        self.move_count = 1

    def load_from_fen(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        '''Loads the board from a FEN string'''
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

    def print_board(self):
        '''Prints the board to the console'''
        # from os import system, name
        # system('cls' if name == 'nt' else 'clear') # Clear the terminal output
        print(" +--+--+--+--+--+--+--+--+")
        row_num = 8
        for i in range(7, -1, -1): # Prints the board
            print(str(row_num)+"|", end="")
            for j in range(8):
                current = self.board[i*8 + j]
                try:
                    print(f"{current.get_colour()}{current.get_type()}|", end="")
                except AttributeError:
                    print("  |", end="")
            print("\n +--+--+--+--+--+--+--+--+")
            row_num -= 1
        print(f"  a  b  c  d  e  f  g  h\t{self.turn.upper()}'s turn")

    def move(self, start: tuple, end: tuple):
        '''Moves the piece from start to end, assuming valid move'''
        working_index = start[0]*8 + start[1]
        working_index = start[0]*8 + start[1] # Puts the coordinate format into the correct format for indexing the array
        working = self.board[working_index]
        target_index = end[0]*8 + end[1]
        target = self.board[target_index]

        valid =  working.is_valid(working, target, working_index, target_index, self.turn, self.board) # Checks move validity
        print(valid)
        
        if valid: # Makes the move
            self.log(end, target)
            self.board[target_index] = working
            self.board[working_index] = Empty()
            self.turn = 'B' if self.turn == 'W' else 'W'
            self.move_count += 1 if self.turn == 'B' else 0
        else:
            print("Invalid move")

    def is_won(self):
        '''Evaluates whether the game is won'''
        return False

    def log(self, end: tuple, target) -> None:
        '''Writes the move to a log file in PGN format'''
        with open(r'/Users/edwardbaker/Documents/nea/chess/output/log.log', 'a+', encoding="utf-8") as log:
            if self.turn == 'w':
                log.write(f"{self.move_count}. {target.get_type() if target.get_type() != 'P' else ''}{chr(end[1]+97)}{end[0]+1} ")
            else:
                log.write(f"{target.get_type() if target.get_type() != 'P' else ''}{chr(end[1]+97)}{end[0]+1}" + "\n")

if __name__ == '__main__':
    print("File run incorrectly - please run game.py instead")
