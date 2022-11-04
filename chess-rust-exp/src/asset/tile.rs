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
    pub fn new(colour: bool, piece: char) -> Tile {
        Tile {
            colour: match colour {
                true => Colour::White,
                false => Colour::Black,
            },
            piece: match piece {
                'p' => Some(Piece::Pawn),
                'n' => Some(Piece::Knight),
                'b' => Some(Piece::Bishop),
                'r' => Some(Piece::Rook),
                'q' => Some(Piece::Queen),
                'k' => Some(Piece::King),
                _ => None,
            },
        }
    }

    pub fn set_colour(&mut self, colour: bool) {
        self.colour = match colour {
            true => Colour::White,
            false => Colour::Black,
        };
    }

    pub fn set_piece(&mut self, piece: char) {
        self.piece = match piece {
            'p' => Some(Piece::Pawn),
            'n' => Some(Piece::Knight),
            'b' => Some(Piece::Bishop),
            'r' => Some(Piece::Rook),
            'q' => Some(Piece::Queen),
            'k' => Some(Piece::King),
            _ => None,
        };
    }

    pub fn get_colour(&self) -> char {
        match self.colour {
            Colour::White => 'W',
            Colour::Black => 'B',
        }
    }

    pub fn get_piece(&self) -> char {
        match self.piece {
            Some(Piece::Pawn) => 'P',
            Some(Piece::Knight) => 'N',
            Some(Piece::Bishop) => 'B',
            Some(Piece::Rook) => 'R',
            Some(Piece::Queen) => 'Q',
            Some(Piece::King) => 'K',
            None => ' ',
        }
    }
}
