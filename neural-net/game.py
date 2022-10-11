import os
from piece import Piece

class Board:
    def __init__(self):
        # Create board with following structure, with each piece being an instance of the Piece class
        """
        ['BR', 'BN', 'BB', 'BK', 'BQ', 'BB', 'BN', 'BR']
        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP']
        ['WR', 'WN', 'WB', 'WK', 'WQ', 'WB', 'WN', 'WR']
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
        start = list(input("Enter the starting position (eg a1): ").strip().lower())
        end = list(input("Enter the ending position (eg h8): ").strip().lower())
        # Format the input to be in the correct format for list references
        current[1], target[1] = chars[start[0]], chars[end[0]]
        current[0], target[0] = int(start[1])-1, int(end[1])-1
        working = self.board[current[0]][current[1]]
        # Check if the move is legal
        if working.check_move(target):
            # If it is, make the move
            working.make_move([target[0], target[1]], turn)
            self.board[current[0]][current[1]] = '  '
            self.board[target[0]][target[1]] = working
        won = check_win(self.board)


def check_win(board) -> int: # This function might need to be rewrittin to be more efficient
    black = white = True
    for row in board:
        for piece in row:
            try:
                if piece.colour == 'B' and piece.type == 'K':
                    white = False
                    break
            except AttributeError:
                continue
        else:
            continue
        break
    for row in board:
        for piece in row:
            try:
                if piece.colour == 'W' and piece.type == 'K':
                    black = False
                    break
            except AttributeError:
                continue
        else:
            continue
        break

    if white and black:
        return 3
    elif white:
        return 1
    elif black:
        return 2
    else:
        return 0



def main():
    board = Board() # Create a blank board
    won = 0
    """
    won can be one of 4 values:
    0: Game is not won
    1: White won
    2: Black won
    3: Draw
    """
    move_num = 0
    while not won: # Runs until someone wins/draws
        move_num += 1
        board.output()
        print(f"\tMove {move_num} | White")
        board.move("W")
        board.output()
        print(f"\tMove {move_num} | Black")
        board.move("B")
    if won == 1:
        print("White won!")
    elif won == 2:
        print("Black won!")
    else:
        print("Draw!")
        

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') # Clearing output
    with open("log.txt", "w"):
        pass   # Clears the logging file each time the program is run
    main()

""" 
TODO
 - Add check
 - Add file logging
 - Add checking of move legality
 - Add checking of checkmate

 - Add checking of stalemate

 - Add castling
 - Add promoting

 - Add checking of insufficient material
 - Add checking of 50-move rule
 - Add checking of threefold repetition
"""