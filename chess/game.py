def process(coordinate: str) -> tuple:
    print(int(coordinate[1]) - 1, 104 - ord(coordinate[0]))
    return (int(coordinate[1]) - 1, 104 - ord(coordinate[0]))

def turn(board) -> bool:
    start = process(input("Enter start position (eg a1): "))
    end = process(input("Enter end position (eg h8): "))

    board.move(start, end)
    won = board.isWon()

    return won

def main():
    board = Board()

    board.loadFromFen()
    won = False
    
    while not won:
        board.printBoard()
        won = turn(board)

if __name__ == '__main__':
    from board import Board
    from piece import Piece

    main()
else:
    print("File run incorrectly")