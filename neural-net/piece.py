class Piece:
    def __init__(self, colour, x, y, types):
        self.colour = colour
        self.x = x
        self.y = y
        self.prevx = -1
        self.prevy = -1
        self.type = types

    def make_move(self, x, y, run) -> tuple:
        if run == "R":
            self.prevx, self.prevy = str(self.x), str(self.y)
            self.x, self.y = x, y

    # Check if a move is legal
    def check_move(self, move):
        if move[0] == "P":
            return self.is_legal_pawn(move)
        elif move[0] == "N":
            return self.is_legal_knight(move)
        elif move[0] == "B":
            return self.is_legal_bishop(move)
        elif move[0] == "R":
            return self.is_legal_rook(move)
        elif move[0] == "Q":
            return self.is_legal_queen(move)
        elif move[0] == "K":
            return self.is_legal_king(move)
        else:
            return False

    def is_legal_pawn(move):
        # Check if move is legal for a pawn
        return True
    
    def is_legal_knight(move):
        # Check if move is legal for a knight
        return True

    def is_legal_bishop(move):
        # Check if move is legal for a bishop
        return True
    
    def is_legal_rook(move):
        # Check if move is legal for a rook
        return True
    
    def is_legal_queen(move):
        # Check if move is legal for a queen
        return True
    
    def is_legal_king(move):
        # Check if move is legal for a king
        return True
    