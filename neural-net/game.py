class Board:
    def __init__(self):
        # Create board with following structure, with each piece being an instance of the Piece class
        """
        ['WR', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR']
        ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP']
        ['BR', 'BN', 'BB', 'BK', 'BQ', 'BB', 'BN', 'BR']
        """

        order = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        self.board = []

        self.board.append([Piece('W', 0, i, order[i]) for i in range(8)])
        self.board.append([Piece('W', 1, i, 'P') for i in range(8)])
        for i in range(2, 6):
            self.board.append(['  ' for i in range(8)])
        self.board.append([Piece('B', 6, i, 'P') for i in range(8)])
        self.board.append([Piece('B', 7, i, order[i]) for i in range(8)])

    def output(self):
        # Printing the board using a reverse order so that the white pieces are on the bottom
        for i, row in enumerate(self.board[::-1]):
            print(" +----+----+----+----+----+----+----+----+")
            print(f"{8-i}|", end='')
            for piece in row:
                # Prints the piece if it exists, otherwise prints a blank space
                try:
                    print(f" {piece.colour}{piece.type} |", end='')
                except AttributeError:
                    print("    |", end='')
            print("\n", end='')
        print(" +----+----+----+----+----+----+----+----+")
        print("    a    b    c    d    e    f    g    h")


class Piece:
    def __init__(self, colour, x, y, type):
        self.colour = colour
        self.x = x
        self.y = y
        self.type = type

    def move(self, x, y):
        pass


game = Board()
game.output()
