use std::fmt::{Display, Formatter};

#[derive(Copy, Clone)]
pub struct Piece {
    kind: char,
    colour: char,
}

impl Piece {
    pub fn new(kind: char, colour: char) -> Piece {
        Piece { kind, colour }
    }

    pub fn get_kind(&self) -> char {
        self.kind
    }

    pub fn get_colour(&self) -> char {
        self.colour
    }

    pub fn is_valid(
        &working_index: &usize,
        &target_index: &usize,
        &turn: &char,
        board: &Vec<Piece>,
    ) -> bool {
        true
    }
}

impl Display for Piece {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result<(), std::fmt::Error> {
        write!(f, "{}{}", self.colour, self.kind)
    }
}
