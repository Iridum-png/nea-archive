def process(coordinate: str) -> tuple:
     # Convert board coordinates into array index
    return (int(coordinate[1]) - 1, ord(coordinate[0]) - 97)

def resetTurn(board) -> None:
    board.printBoard()
    turn(board)

def turn(board) -> bool:
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    start = input("Enter start position (eg a1): ")
    try:
        if start[0] in valid_letters:
            start = process(start)
        else:
            resetTurn(board)
        end = input("Enter end position (eg h8): ")
        if end[0] in valid_letters:
            end = process(end)
        else:
            resetTurn(board)
    except IndexError:
        resetTurn(board)

    board.move(start, end)
    return board.isWon()

def main():
    board = Board()

    board.loadFromFen()
    won = False

    while not won:
        # board.debugPrint()
        board.printBoard()
        won = turn(board)

if __name__ == '__main__':
    from board import Board
    from piece import Piece

    main()
else:
    print("File run incorrectly")
