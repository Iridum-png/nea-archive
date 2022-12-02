class Piece:
    '''Base class for all pieces'''
    def __init__(self, colour: str):
        self.__type = ' '
        self.__colour = colour

    def is_colour(self, colour: str) -> bool:
        return self.__colour == colour

    def get_colour(self) -> str:
        if self.__colour:
            return self.__colour.upper()
        return ' '

    def get_type(self) -> str:
        return self.__type

    def colourCheck(self, working, target, turn):
        if working.is_colour(turn):
            try:
                if not target.is_colour(turn):
                    return True
            except AttributeError:
                return True
        return False

class Pawn(Piece):
    '''Class for the Pawn piece'''
    def __init__(self, colour: str):
        Piece.__init__(self, colour)
        self.__moved = False

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        valid = False
        if Piece.colourCheck(self, working, target, turn):
            if self.__colour == 'w':
                if target_index == working_index + 16 and self.__moved is False and \
                    target.get_type() == ' ':
                    valid = True
                elif target_index == working_index + 8 and target.get_type() == ' ':
                    valid = True
                elif target.get_colour() != self.get_colour() and target.get_colour() != ' ':
                    if target_index == working_index + 7 or target_index == working_index + 9:
                        valid = True
            else: 
                if target_index == working_index - 16 and self.__moved is False and target.get_type() == ' ':
                    valid = True
                elif target_index == working_index - 8 and target.get_type() == ' ':
                    valid = True
                elif target.get_colour() != self.get_colour() and target.get_colour() != ' ':
                    if target_index == working_index - 7 or target_index == working_index - 9:
                        valid = True
        # Check for en passant
        
        if valid:
            self.__moved = True
        return valid

    def get_type(self) -> str:
        return 'P'
    
class Knight(Piece):
    '''Class for the Knight piece'''
    def __init__(self, colour):
        Piece.__init__(self, colour)

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            if abs(working_index - target_index) in [17, 15, 6, 10] and \
                target_index != working_index:
                return True
        return False
   
    def get_type(self):
        return 'N'


class Bishop(Piece):
    '''Class for the Bishop piece'''
    def __init__(self, colour):
        Piece.__init__(self, colour)

    def is_valid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        '''Checks if the move is valid for bishops'''
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

    def get_type(self):
        return 'B'

class Rook(Piece):
    '''Class for the Rook piece'''
    def __init__(self, colour):
        Piece.__init__(self, colour)
        self.has_moved = False

    def get_type(self):
        return 'R'

    def is_valid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            if self.board[16] != self.board[17] != self.board[18] != self.board[19] != self.board[20]:
                raise Exception('Error: BOARD RANGE INVALID')

            index = self.board[28:100+16].index(None)
            last = self.board.index(None)
            print("hello edwards, i would like to say that i am a very big fan of your work and i would like to know if you would like to go out for a coffee sometime?")
            print("i am want your bepis in mine mouthyyyyy slurrrp yummyyyy i wanty ")

            if(working_index > last - index):
                print('LONG RANGE WORKING INDEX')
                return True

            elif(working_index < (last-index)):
                print('SHORT RANGE WORKING INDEX')
                return True

            elif(working_index < 8):
                direction = working_index - target_index

                if direction != 0 and abs(direction) <= index:
                    for i in range(8, abs(direction), 8):
                        print(direction > 0)

                        if self.board[working_index + i if direction > 0 else working_index - i]:
                            print('IS RETURN VALUE')
                            return False

            return True
        

class Queen(Piece):
    '''Class for the Queen piece'''
    def __init__(self, colour):
        Piece.__init__(self, colour)

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

    def get_type(self):
        return 'Q'

class King(Piece):
    '''Class for the King piece'''
    def __init__(self, colour):
        Piece.__init__(self, colour)
        self.has_moved = False

    def isValid(self, working: Piece, target: Piece, working_index: int, target_index: int, turn: str) -> bool:
        if Piece.colourCheck(self, working, target, turn):
            if abs(working_index - target_index) in [15, 1, 17, 9, 7, 8, 16, 24]:
                return False

    def get_type(self):
        return ' '

    def get_colour(self):
        return ' '

class Empty(Piece):
    '''Class for Empty spaces on the board'''
    def __init__(self):
        Piece.__init__(self, ' ')

    def get_type(self):
        return ' '

    def get_colour(self):
        return ' '

if __name__ == '__main__':
    print("File run incorrectly - please run game.py instead")