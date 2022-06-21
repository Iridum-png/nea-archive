import os

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
        print("\n")
        os.system('cls' if os.name == 'nt' else 'clear')
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
        print("    a    b    c    d    e    f    g    h", end='')

    def move(self):
        chars = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        current = ['', '']
        target = ['', '']
        start = list(input("Enter the starting position (eg a1): ").strip())
        end = list(input("Enter the ending position (eg h8): ").strip())
        # Format the input to be in the correct format for list references
        current[1], target[1] = chars[start[0]], chars[end[0]]
        current[0], target[0] = int(start[1])-1, int(end[1])-1

        if self.check():
            self.board[target[0]][target[1]] = self.board[current[0]][current[1]]
            self.board[current[0]][current[1]] = '  '
        else:
            print("Invalid move")
            self.move()

    def check(self) -> bool:
        return True

class Piece:
    def __init__(self, colour, x, y, type):
        self.colour = colour
        self.x = x
        self.y = y
        self.type = type

    def make_move(self, x, y):
        pass


def check_win(board) -> bool:
    from random import choice
    return choice([True, False])


def main():
    board = Board()
    won = False
    move_num = 0
    while not won:
        move_num += 1
        board.output()
        print(f"\tMove {move_num} | White")
        board.move()
        board.output()
        print(f"\tMove {move_num} | Black")
        board.move()
        check_win(board)

os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "__main__":
    main()
