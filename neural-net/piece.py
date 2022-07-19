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

    def check_move(self, turn, colour) -> bool:
        if turn != colour:
            return False

        if self.type == "P":
            return False
        return True