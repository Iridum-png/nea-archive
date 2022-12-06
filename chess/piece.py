from __future__ import annotations

class Square:
    '''Base class for all squares'''
    def __init__(self, colour: str):
        self.__type = ' '
        self.__colour = colour

    def is_colour(self, colour: str) -> bool:
        return self.__colour == colour

    def get_colour(self) -> str:
        if self.__colour:
            return self.__colour
        return ' '

    def get_type(self) -> str:
        return self.__type

    def colour_check(self, working: Square, target: Square, turn: str) -> bool: # NOTE - Can't type hint working or target here correctly for some reason
        if working.is_colour(turn):
            try:
                if not target.is_colour(turn):
                    return True
            except AttributeError:
                return True
        return False

class Pawn(Square):
    '''Class for the Pawn Piece'''
    def __init__(self, colour: str):
        super().__init__(colour)
        self.__moved = False

    def is_valid(self, working: Square, target: Square, working_index: int, target_index: int, turn: str, board: list) -> bool: # TODO en passant
        valid = False
        if Square.colour_check(self, working, target, turn):
            print("Correct colour chosen")
            if self.get_colour() == 'W': # Logic for white's movement
                if target_index == working_index + 16 and not self.__moved and target.getType() == ' ': # Logic for moving forwards 2 squares
                    valid = True
                elif target_index == working_index + 8 and target.getType() == ' ': # Logic for moving forwards 1 sqaure
                    valid = True
                elif target.get_colour() != self.get_colour() and target.get_colour() != ' ': # Logic for taking Square
                    if target_index == working_index + 7 or target_index == working_index + 9:
                        valid = True
            else: # Logic for black's movement
                if target_index == working_index - 16 and not self.__moved and target.getType() == ' ': # Logic for moving forward 2 squares
                    valid = True
                elif target_index == working_index - 8 and target.getType() == ' ': # Logic for moving forward one square
                    valid = True
                elif target.get_colour() != self.get_colour() and target.get_colour() != ' ': # Logic for taking a Square
                    if target_index == working_index - 7 or target_index == working_index - 9:
                        valid = True
        # Check for en passant
        
        if valid and not self.__moved:
            self.__moved = True
        return valid

    def get_type(self) -> str:
        return 'P'

class Knight(Square):
    '''Class for the Knight Piece'''
    def __init__(self, colour):
        super().__init__(colour)

    def is_valid(self, working: Square, target: Square, working_index: int, target_index: int, turn: str, board: list) -> bool:
        if Square.colour_check(self, working, target, turn):
            if abs(working_index - target_index) in [17, 15, 6, 10] and \
                target_index != working_index:
                return True
        return False
    
    def get_type(self):
        return 'N'

class Bishop(Square):
    '''Class for the Bishop Piece'''
    def __init__(self, colour):
        super().__init__(colour)

    def is_valid(self, working: Square, target: Square, working_index: int, target_index: int, turn: str, board: list) -> bool:
        '''Checks if the move is valid for bishops'''
        if Square.colour_check(self, working, target, turn):
            direction = working_index - target_index
            if abs(direction) % 7 == 0:
                for i in range(7, abs(direction), 7):
                    if board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
            elif abs(direction) % 9 == 0:
                for i in range(9, abs(direction), 9):
                    if board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
        return False

    def get_type(self):
        return 'B'

class Rook(Square):
    '''Class for the Rook Piece'''
    def __init__(self, colour):
        super().__init__(colour)
        self.has_moved = False

    def is_valid(self, working: Square, target: Square, working_index: int, target_index: int, turn: str, board: list) -> bool:
        if Square.colour_check(self, working, target, turn):
            direction = working_index - target_index
            if abs(direction) % 8 == 0:
                for i in range(8, abs(direction), 8):
                    if board[working_index + i if direction > 0 else working_index - i]:
                        return False
            elif abs(direction) % 1 == 0:
                for i in range(1, abs(direction), 1):
                    if board[working_index + i if direction > 0 else working_index - i]:
                        return False
            return True
        return False
        # Check for piece collisions in the move
        
    def get_type(self):
        return 'R'
        

class Queen(Square):
    '''Class for the Queen Piece'''
    def __init__(self, colour):
        super().__init__(colour)

    def is_valid(self, working: Square, target: Square, working_index: int, target_index: int, turn: str, board: list) -> bool:
        if Square.colour_check(self, working, target, turn):
            direction = working_index - target_index
            if abs(direction) % 7 == 0:
                for i in range(7, abs(direction), 7):
                    if board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
            elif abs(direction) % 9 == 0:
                for i in range(9, abs(direction), 9):
                    if board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
            elif abs(direction) % 8 == 0:
                for i in range(8, abs(direction), 8):
                    if board[working_index + i if direction > 0 else working_index - i]:
                        return False
                return True
        return False

    def get_type(self):
        return 'Q'

class King(Square):
    '''Class for the King Piece'''
    def __init__(self, colour):
        super().__init__(colour)
        self.has_moved = False

    def is_valid(self, working: Square, target: Square, working_index: int, target_index: int, turn: str) -> bool:
        if Square.colour_check(self, working, target, turn):
            if abs(working_index - target_index) in [15, 1, 17, 9, 7, 8, 16, 24]:
                return False
    
    def get_type(self):
        return 'K'

class Empty(Square):
    '''Class for Empty spaces on the board'''
    def __init__(self):
        Square.__init__(self, ' ')

    def get_type(self):
        return ' '

    def get_colour(self):
        return ' '

if __name__ == '__main__':
    print("File run incorrectly - please run game.py instead")