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

    def move(self, turn):
        chars = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        current = ['', '']
        target = ['', '']
        start = list(input("Enter the starting position (eg a1): ").strip())
        end = list(input("Enter the ending position (eg h8): ").strip())
        # Format the input to be in the correct format for list references
        current[1], target[1] = chars[start[0]], chars[end[0]]
        current[0], target[0] = int(start[1])-1, int(end[1])-1
        working = self.board[current[0]][current[1]]

        if check_win(self.board) != 'N':
            print("Checkmate!")
            won()
        try:
            _ = working.make_move(target[0], target[1],"S")
        except AttributeError:
            print("Invalid move - no piece at this position")
            self.move()
        else:
            if self.check_move(turn, working.colour):
                working.make_move(target[1], target[0], "R")
                with open ("log.txt", "a") as f:
                    f.write(f"{working.prevx},{working.prevy}->{working.x},{working.y} {working.colour}{working.type}\n")

                self.board[target[0]][target[1]], self.board[current[0]][current[1]] = working, '  '
            else:
                print("Invalid move - move not allowed")
                self.move(turn)

    def check_move(self, turn, colour) -> bool:
        if turn != colour:
            return False
        return True

class Piece:
    def __init__(self, colour, x, y, type):
        self.colour = colour
        self.x = x
        self.y = y
        self.prevx = -1
        self.prevy = -1
        self.type = type

    def make_move(self, x, y, run) -> tuple:
        if run == "R":
            self.prevx, self.prevy = str(self.x), str(self.y)
            self.x, self.y = x, y


def check_win(board) -> str:
    black = True
    white = True
    for row in board:
        for piece in row:
            try:
                if piece.colour == 'W' and piece.type == 'K':
                    black = False
                elif piece.colour == 'B' and piece.type == 'K':
                    white = False
            except AttributeError:
                continue
    return "B" if black else "W" if white else "D" if black and white else "N" # This return system sucks


def won():
    pass


def main():
    board = Board()
    won = False
    move_num = 0
    while not won:
        move_num += 1
        board.output()
        print(f"\tMove {move_num} | White")
        board.move("W")
        board.output()
        print(f"\tMove {move_num} | Black")
        board.move("B")
        

os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "__main__":
    with open("log.txt", "w"):
        pass   # Clears the logging file each time the program is run
    main()

# check_win() change return system
# make_move() weird variable issue