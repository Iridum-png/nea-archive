from piece import Piece

class Board:
    def __init__(self):
        self.board = []

    def loadFromFen(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        piece_type_from_symbol = {'k': 'king', 'q': 'queen', 'r': 'rook', 'b': 'bishop', 'n': 'knight', 'p': 'pawn'}
        
        fenBoard = fen.split(' ')[0]
        
        column = 0
        row = 7

        for symbol in fenBoard:
            if symbol == '/':
                column = 0
                row -= 1
            elif symbol.isdigit():
                column += int(symbol)
                for _ in range(int(symbol)):
                    self.board.append('    ')
            else:
                pieceColour = 'white' if symbol.isupper() else 'black'
                pieceType = piece_type_from_symbol[symbol.lower()]
                self.board.append(Piece(pieceColour, pieceType))
                column += 1

    def printBoard(self): # Work in progress
        self.clear()
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
        print("  a  b  c  d  e  f  g  h")

    def clear(self):
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    print("File run incorrectly")