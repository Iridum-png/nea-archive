def main():
    board = Board()

    board.loadFromFen()
    board.printBoard()

if __name__ == '__main__':
    from board import Board
    from piece import Piece

    main()
    
else:
    print("File run incorrectly")