class Piece:
    def __init__(self, colour: str):
        self.__type = ' '
        self.__colour = colour

    def isColour(self, colour: str) -> bool:
        print(self.__colour, colour)
        return self.__colour == colour

    def getColour(self) -> str:
        if self.__colour:
            return self.__colour
        return ' '

    def getType(self):
        return self.__type

    def colourCheck(self, working, target, turn: str) -> bool: # NOTE - Can't type hint working or target here correctly for some reason
        print(f"{working.isColour(turn)}, {target.isColour(turn)}")
        if working.isColour(turn):
            try:
                if not target.isColour(turn):
                    return True
            except AttributeError:
                return True
        return False

class Pawn(Piece):
    def __init__(self, colour: str):
        Piece.__init__(self, colour)
        self.__moved = False

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str, board: list) -> bool: # TODO en passant
        valid = False
        if Piece.colourCheck(self, working, target, turn):
            if self.getColour() == 'W': # Logic for white's movement
                if target_index == working_index + 16 and self.__moved == False and target.getType() == ' ': # Logic for moving forwards 2 squares
                    valid = True
                elif target_index == working_index + 8 and target.getType() == ' ': # Logic for moving forwards 1 sqaure
                    valid = True
                elif target.getColour() != self.getColour() and target.getColour() != ' ': # Logic for taking piece
                    if target_index == working_index + 7 or target_index == working_index + 9:
                        valid = True
            else: # Logic for black's movement
                if target_index == working_index - 16 and self.__moved == False and target.getType() == ' ': # Logic for moving forward 2 squares
                    valid = True
                elif target_index == working_index - 8 and target.getType() == ' ': # Logic for moving forward one square
                    valid = True
                elif target.getColour() != self.getColour() and target.getColour() != ' ': # Logic for taking a piece
                    if target_index == working_index - 7 or target_index == working_index - 9:
                        valid = True
        # Check for en passant
        
        if valid and not self.__moved:
            self.__moved = True
        return valid

    def getType(self) -> str:
        return 'P'

class Knight(Piece):
    def __init__(self, colour):
        Piece.__init__(self, colour)

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            if abs(working_index - target_index) in [17, 15, 6, 10] and target_index != working_index:
                return True
        return False
    
    def getType(self):
        return 'N'

class Bishop(Piece):
    def __init__(self, colour):
        Piece.__init__(self, colour)
        self.__type = 'B'

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            direction = working_index - target_index
            if abs(direction) % 7 == 0:
                for i in range(7, abs(direction), 7):
                    if self.board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
            elif abs(direction) % 9 == 0:
                for i in range(9, abs(direction), 9):
                    if self.board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
        return False

    def getType(self):
        return 'B'

class Rook(Piece):
    def __init__(self, colour):
        Piece.__init__(self, colour)
        self.__type = 'R'
        self.has_moved = False

    def getType(self):
        return 'R'

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            if self.board[16] != self.board[17] != self.board[18] != self.board[19] != self.board[20]:
                raise Exception('Error: BOARD RANGE INVALID')

            range = self.board[28:100+16].index(None)
            last = self.board.index(None)

            if(working_index > last - range):
                print('LONG RANGE WORKING INDEX')
                return True

            elif(working_index < (last-range)):
                print('SHORT RANGE WORKING INDEX')
                return True

            elif(working_index < 8):
                direction = working_index - target_index

                if direction != 0 and abs(direction) <= range:
                    for i in range(8, abs(direction), 8):
                        print(direction > 0)

                        if self.board[working_index + i if direction > 0 else working_index - i]:
                            print('IS RETURN VALUE')
                            return False

            return True
        

class Queen(Piece):
    def __init__(self, colour):
        Piece.__init__(self, colour)
        self.__type = 'Q'

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            direction = working_index - target_index
            if abs(direction) % 7 == 0:
                for i in range(7, abs(direction), 7):
                    if self.board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
            elif abs(direction) % 9 == 0:
                for i in range(9, abs(direction), 9):
                    if self.board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
            elif abs(direction) % 8 == 0:
                for i in range(8, abs(direction), 8):
                    if self.board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
        return False

    def getType(self):
        return 'Q'

class King(Piece):
    def __init__(self, colour):
        Piece.__init__(self, colour)
        self.has_moved = False

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            if abs(working_index - target_index) in [15, 1, 17, 9, 7, 8, 16, 24]:
                return False
    
    def getType(self):
        return 'K'

class Empty(Piece):
    def __init__(self):
        Piece.__init__(self, ' ')

    def getType(self):
        return ' '

    def getColour(self):
        return ' '

if __name__ == '__main__':
    print("File run incorrectly - please run game.py instead")