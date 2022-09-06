class Piece:
    def __init__(self, colour: str, value: str='none'):
        """
        Leftmost 2 bits represent the piece colour, either 01 for white or 10 for black
        Rightmost 3 bits represent the piece type, 001 for pawn, 010 for knight, 011 for bishop, 100 for rook, 101 for queen, 110 for king
        This might be making the program too complicated - will remove if it doesn't pay off in the end
        """
        self.values = {
            'none': 0,
            'king': 1,
            'pawn': 2,
            'knight': 3,
            'bishop': 4,
            'rook': 5,
            'queen': 6,
            'white': 8,
            'black': 16
        }
        self.type_mask = 0b00111
        self.colour_mask = 0b11000
        self.value = self.values[value] + self.values[colour]

    def isColour(self, colour):
        return (self.value & self.colour_mask) == self.values[colour]

    def getColour(self):
        if self.value & self.colour_mask == 8:
            return 'W'
        else:
            return 'B'

    def getType(self):
        values = [value for value in self.values.values()] # Terrible variable naming
        keys = [key for key in self.values.keys()]
        value = self.value & self.type_mask
        if keys[values.index(value)][0] == 'k':
            prefix = 'k' if keys[values.index(value)][-1] == 'g' else 'n'
        else:
            prefix = keys[values.index(value)][0]
        return prefix.upper()

if __name__ == '__main__':
    print("File run incorrectly")