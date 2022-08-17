class Piece:
    # none = 0
    # king = 1
    # pawn = 2
    # knight = 3
    # bishop = 4
    # rook = 5
    # queen = 6
    # white = 8
    # black = 16
    def __init__(self, value: str, colour: str):
        """
        Leftmost 2 bits represent the piece colour, either 01 for white or 10 for black
        Rightmost 3 bits represent the piece type, 001 for pawn, 010 for knight, 011 for bishop, 100 for rook, 101 for queen, 110 for king
        """
        self.values = {'none': 0, 'p': 1, 'n': 2, 'b': 3, 'r': 4, 'q': 5, 'k': 6, 'white': 8, 'black': 16}
        self.typeMask = 0b111
        white_mask = 0b01000
        black_mask = 0b10000
        self.colour_mask = white_mask | black_mask
        self.value = self.values[value] + self.values[colour]

    def isColour(self, colour):
        return (self.value & self.colour_mask) == self.values[colour]

    def colour(self):
        return (self.value & self.colour_mask)
