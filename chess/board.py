from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.turn = 'w'

    def loadFromFen(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        piece_type_from_symbol = {'k': 'king', 'q': 'queen', 'r': 'rook', 'b': 'bishop', 'n': 'knight', 'p': 'pawn'}
        
        fen_board = fen.split(' ')[0]
        
        column = 0
        row = 7

        for symbol in fen_board:
            if symbol == '/':
                column = 0
                row -= 1
            elif symbol.isdigit():
                column += int(symbol)
                for _ in range(int(symbol)):
                    self.board.append('    ')
            else:
                piece_colour = 'white' if symbol.isupper() else 'black'
                piece_type = piece_type_from_symbol[symbol.lower()]
                self.board.append(Piece(piece_colour, piece_type))
                column += 1
        print(self.board)

    def printBoard(self): # Work in progress
        from os import system, name
        # system('cls' if name == 'nt' else 'clear')
        print(" +--+--+--+--+--+--+--+--+")
        row_num = 8
        for i in range(8):
            print(str(row_num)+"|", end="")
            for j in range(8):
                try:
                    current = self.board[i*8 + j]
                    print(f"{current.getColour()}{current.getType()}|", end="")
                except AttributeError:
                    print("  |", end="")
            print("\n +--+--+--+--+--+--+--+--+")
            row_num -= 1
        print(f"  a  b  c  d  e  f  g  h\t{self.turn}")

    def move(self, start: tuple, end: tuple):
        working_piece_index = start[0]*8 + start[1]
        working_piece = self.board[working_piece_index]
        target_index = end[0]*8 + end[1]
        print(working_piece.getColour() + working_piece.getType())

        self.board[target_index] = working_piece
        self.board[working_piece_index] = '    '


        self.turn = 'b' if self.turn == 'w' else 'w'

    def isWon(self):
        return False

if __name__ == '__main__':
    print("File run incorrectly")