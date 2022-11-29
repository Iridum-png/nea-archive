from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King, Empty

class Board:
    def __init__(self):
        self.board = []
        self.turn = 'w'
        self.move_count = 1

    def loadFromFen(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        piece_type_from_symbol = {'k': King, 'q': Queen, 'r': Rook, 'b': Bishop, 'n': Knight, 'p': Pawn}
        
        fen_board = fen.split(' ')[0][::-1].split('/')
        
        for rows in fen_board:
            for symbol in rows[::-1]:
                if symbol.isdigit():
                    for _ in range(int(symbol)):
                        self.board.append(Empty())
                else:
                    piece_colour = 'w' if symbol.isupper() else 'b'
                    piece_type = piece_type_from_symbol[symbol.lower()]
                    self.board.append(piece_type(piece_colour))
        self.turn = fen.split(' ')[1]

    def printBoard(self):
        # from os import system, name
        # system('cls' if name == 'nt' else 'clear')
        print(" +--+--+--+--+--+--+--+--+")
        row_num = 8
        for i in range(7, -1, -1):
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
        working_index = start[0]*8 + start[1]
        working = self.board[working_index]
        target_index = end[0]*8 + end[1]
        target = self.board[target_index]

        check =  working.isValid(working, target, working_index, target_index, self.turn, self.board)
        if check:
            self.log(end, target)
            self.board[target_index] = working
            self.board[working_index] = Empty()
            self.turn = 'b' if self.turn == 'w' else 'w'
            self.move_count += 1 if self.turn == 'b' else 0
        else:
            print("Invalid move")
        if check[1]:
            self.board = check[1]

    def is_won(self):
        return False

    def log(self, end: tuple, target) -> None:
        '''Writes the move to a log file in PGN format'''
        with open(r'/Users/edwardbaker/Documents/nea/chess/output/log.log', 'a+') as log:
            if self.turn == 'w':
                log.write(f"{self.move_count}. {target.get_type() if target.get_type() != 'P' else ''}{chr(end[1]+97)}{end[0]+1} ")
            else:
                log.write(f"{target.get_type() if target.get_type() != 'P' else ''}{chr(end[1]+97)}{end[0]+1}" + "\n")

if __name__ == '__main__':
    print("File run incorrectly - please run game.py instead")
