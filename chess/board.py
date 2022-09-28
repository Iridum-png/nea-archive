from piece import Piece
from game import Game

class Board:
    def __init__(self):
        self.board = []
        self.turn = 'w'

    def loadFromFen(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):
        piece_type_from_symbol = {'k': 'king', 'q': 'queen', 'r': 'rook', 'b': 'bishop', 'n': 'knight', 'p': 'pawn'}
        
        fen_board = fen.split(' ')[0][::-1]
        
        column = 0
        row = 7

        for symbol in fen_board:
            if symbol == '/':
                column = 0
                row -= 1
            elif symbol.isdigit():
                column += int(symbol)
                for _ in range(int(symbol)):
                    self.board.append(Piece('none', 'none'))
            else:
                piece_colour = 'w' if symbol.isupper() else 'b'
                piece_type = piece_type_from_symbol[symbol.lower()]
                self.board.append(Piece(piece_colour, piece_type))
                column += 1

    def printBoard(self):
        from os import system, name
        # system('cls' if name == 'nt' else 'clear')
        print(" +--+--+--+--+--+--+--+--+")
        row_num = 8
        for i in range(7, -1, -1):
            print(str(row_num)+"|", end="")
            for j in range(7, -1, -1):
                current = self.board[i*8 + j]
                try:
                    print(f"{current.getColour()}{current.getType()}|", end="")
                except AttributeError:
                    print("  |", end="")
            print("\n +--+--+--+--+--+--+--+--+")
            row_num -= 1
        print(f"  a  b  c  d  e  f  g  h\t{self.turn}")

    def move(self, start: tuple, end: tuple):
        print(start, end)
        working_index = start[0] + start[1]*8
        working = self.board[working_index]
        target_index = end[0] + end[1]*8
        target = self.board[target_index]

        if working.isValid(working, target, self.turn):
            self.board[target_index] = working
            self.board[working_index] = '    '
            self.turn = 'b' if self.turn == 'w' else 'w'
        else:
            print("Invalid move")

    def isWon(self):
        return False

    def outputPiece(self, piece: Piece) -> str:
        if piece == '    ':
            return '    '
        else:
            return piece.getColour() + piece.getType()

if __name__ == '__main__':
    print("File run incorrectly - please run game.py instead")
