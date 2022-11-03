enum Colour {
    White,
    Black,
}

enum Piece {
    Pawn,
    Knight,
    Bishop,
    Rook,
    Queen,
    King,
}

pub struct Tile {
    colour: Colour,
    piece: Option<Piece>,
}

impl Tile {
    pub fn new() -> Tile {
        Tile {
            colour: Colour::White,
            piece: None,
        }
    }

    pub fn set_colour(&mut self, colour: Colour) {
        self.colour = colour;
    }

    pub fn set_piece(&mut self, piece: Piece) {
        self.piece = Some(piece);
    }
}
