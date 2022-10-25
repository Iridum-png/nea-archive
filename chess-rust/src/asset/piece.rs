pub trait Piece {
    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        board: &[Box<dyn Piece>],
    ) -> bool;
    fn is_colour(&self, colour: char) -> bool;
    fn get_colour(&self) -> char;
    fn get_type(&self) -> char;
    fn box_clone(&self) -> Box<dyn Piece>;
}

impl Clone for Box<dyn Piece> {
    fn clone(&self) -> Box<dyn Piece> {
        self.box_clone()
    }
}

#[derive(Clone)]
struct Data {
    piece: char,
    colour: char,
}

#[derive(Clone)]
struct Pawn {
    data: Data,
    moved: bool,
}

impl Piece for Pawn {
    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        _board: &[Box<dyn Piece>],
    ) -> bool {
        let working_row = working_index / 8;
        let working_col = working_index % 8;
        let target_row = target_index / 8;
        let target_col = target_index % 8;

        let mut valid = false;

        if self.is_colour(turn) {
            if self.is_colour('W') {
                if working_row == 1 {
                    if target_row == 3 && target_col == working_col {
                        valid = true;
                    }
                } else if target_row == working_row + 1 && target_col == working_col {
                    valid = true;
                }
            } else {
                if working_row == 6 {
                    if target_row == 4 && target_col == working_col {
                        valid = true;
                    }
                } else if target_row == working_row - 1 && target_col == working_col {
                    valid = true;
                }
            }
        }

        valid
    }

    fn is_colour(&self, colour: char) -> bool {
        self.get_colour() == colour
    }

    fn get_colour(&self) -> char {
        self.data.colour.to_ascii_uppercase()
    }

    fn get_type(&self) -> char {
        'P'
    }

    fn box_clone(&self) -> Box<dyn Piece> {
        Box::new((*self).clone())
    }
}

impl Pawn {
    fn new(piece: char, colour: char) -> Pawn {
        Pawn {
            data: Data { piece, colour },
            moved: false,
        }
    }
}

#[derive(Clone)]
struct Rook {
    data: Data,
    moved: bool,
}

impl Piece for Rook {
    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        board: &[Box<dyn Piece>],
    ) -> bool {
        let working_row = working_index / 8;
        let working_col = working_index % 8;
        let target_row = target_index / 8;
        let target_col = target_index % 8;

        let mut valid = false;

        if self.is_colour(turn) {
            if working_row == target_row {
                valid = true;
            } else if working_col == target_col {
                valid = true;
            }
        }

        // Check if piece is in way
        if valid {
            if working_row == target_row {
                let mut min = working_col;
                let mut max = target_col;

                if min > max {
                    min = target_col;
                    max = working_col;
                }

                for i in min..max {
                    if board[i + working_row * 8].get_type() != ' ' {
                        valid = false;
                    }
                }
            } else if working_col == target_col {
                let mut min = working_row;
                let mut max = target_row;

                if min > max {
                    min = target_row;
                    max = working_row;
                }

                for i in min..max {
                    if board[working_col + i * 8].get_type() != ' ' {
                        valid = false;
                    }
                }
            }
        }

        valid
    }

    fn is_colour(&self, colour: char) -> bool {
        self.get_colour() == colour
    }

    fn get_colour(&self) -> char {
        self.data.colour.to_ascii_uppercase()
    }

    fn get_type(&self) -> char {
        'R'
    }

    fn box_clone(&self) -> Box<dyn Piece> {
        Box::new((*self).clone())
    }
}

impl Rook {
    fn new(piece: char, colour: char) -> Rook {
        Rook {
            data: Data { piece, colour },
            moved: false,
        }
    }
}

#[derive(Clone)]
struct Knight {
    data: Data,
}

impl Piece for Knight {
    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        _board: &[Box<dyn Piece>],
    ) -> bool {
        let working_row = working_index / 8;
        let working_col = working_index % 8;
        let target_row = target_index / 8;
        let target_col = target_index % 8;

        let mut valid = false;

        if self.is_colour(turn) {
            if (working_row - target_row) == 2 && (working_col - target_col) == 1 {
                valid = true;
            } else if (working_row - target_row) == 1 && (working_col - target_col) == 2 {
                valid = true;
            }
        }

        valid
    }

    fn is_colour(&self, colour: char) -> bool {
        self.get_colour() == colour
    }

    fn get_colour(&self) -> char {
        self.data.colour.to_ascii_uppercase()
    }

    fn get_type(&self) -> char {
        'N'
    }

    fn box_clone(&self) -> Box<dyn Piece> {
        Box::new((*self).clone())
    }
}

impl Knight {
    fn new(piece: char, colour: char) -> Knight {
        Knight {
            data: Data { piece, colour },
        }
    }
}

#[derive(Clone)]
struct Bishop {
    data: Data,
}

impl Piece for Bishop {
    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        board: &[Box<dyn Piece>],
    ) -> bool {
        let working_row = working_index / 8;
        let working_col = working_index % 8;
        let target_row = target_index / 8;
        let target_col = target_index % 8;

        let mut valid = false;

        if self.is_colour(turn) {
            if (working_row - target_row) == (working_col - target_col) {
                valid = true;
            }
        }

        // Check if piece is in way
        if valid {
            let mut min_row = working_row;
            let mut max_row = target_row;
            let mut min_col = working_col;
            let max_col = target_col;

            if min_row > max_row {
                min_row = target_row;
                max_row = working_row;
            }

            if min_col > max_col {
                min_col = target_col;
            }

            for i in 1..(max_row - min_row) {
                if board[(min_col + i) + (min_row + i) * 8].get_type() != ' ' {
                    valid = false;
                }
            }
        }

        valid
    }

    fn is_colour(&self, colour: char) -> bool {
        self.get_colour() == colour
    }

    fn get_colour(&self) -> char {
        self.data.colour.to_ascii_uppercase()
    }

    fn get_type(&self) -> char {
        'B'
    }

    fn box_clone(&self) -> Box<dyn Piece> {
        Box::new((*self).clone())
    }
}

impl Bishop {
    fn new(piece: char, colour: char) -> Bishop {
        Bishop {
            data: Data { piece, colour },
        }
    }
}

#[derive(Clone)]
struct Queen {
    data: Data,
}

impl Piece for Queen {
    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        board: &[Box<dyn Piece>],
    ) -> bool {
        let working_row = working_index / 8;
        let working_col = working_index % 8;
        let target_row = target_index / 8;
        let target_col = target_index % 8;

        let mut valid = false;

        if self.is_colour(turn) {
            if working_row == target_row {
                valid = true;
            } else if working_col == target_col {
                valid = true;
            } else if (working_row - target_row) == (working_col - target_col) {
                valid = true;
            }
        }

        // Check if piece is in way
        if valid {
            if working_row == target_row {
                let mut min = working_col;
                let mut max = target_col;

                if min > max {
                    min = target_col;
                    max = working_col;
                }

                for i in min..max {
                    if board[i + working_row * 8].get_type() != ' ' {
                        valid = false;
                    }
                }
            } else if working_col == target_col {
                let mut min = working_row;
                let mut max = target_row;

                if min > max {
                    min = target_row;
                    max = working_row;
                }

                for i in min..max {
                    if board[working_col + i * 8].get_type() != ' ' {
                        valid = false;
                    }
                }
            } else if (working_row - target_row) == (working_col - target_col) {
                let mut min_row = working_row;
                let mut max_row = target_row;
                let mut min_col = working_col;
                let max_col = target_col;

                if min_row > max_row {
                    min_row = target_row;
                    max_row = working_row;
                }

                if min_col > max_col {
                    min_col = target_col;
                }

                for i in 1..(max_row - min_row) {
                    if board[(min_col + i) + (min_row + i) * 8].get_type() != ' ' {
                        valid = false;
                    }
                }
            }
        }

        valid
    }

    fn is_colour(&self, colour: char) -> bool {
        self.get_colour() == colour
    }

    fn get_colour(&self) -> char {
        self.data.colour.to_ascii_uppercase()
    }

    fn get_type(&self) -> char {
        'Q'
    }

    fn box_clone(&self) -> Box<dyn Piece> {
        Box::new((*self).clone())
    }
}

impl Queen {
    fn new(piece: char, colour: char) -> Queen {
        Queen {
            data: Data { piece, colour },
        }
    }
}

#[derive(Clone)]
struct King {
    data: Data,
    moved: bool,
}

impl Piece for King {
    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        _board: &[Box<dyn Piece>],
    ) -> bool {
        let working_row = working_index / 8;
        let working_col = working_index % 8;
        let target_row = target_index / 8;
        let target_col = target_index % 8;

        let mut valid = false;

        if self.is_colour(turn) {
            if (working_row - target_row) <= 1 && (working_col - target_col) <= 1 {
                valid = true;
            }
        }

        valid
    }

    fn is_colour(&self, colour: char) -> bool {
        self.get_colour() == colour
    }

    fn get_colour(&self) -> char {
        self.data.colour.to_ascii_uppercase()
    }

    fn get_type(&self) -> char {
        'K'
    }

    fn box_clone(&self) -> Box<dyn Piece> {
        Box::new((*self).clone())
    }
}

impl King {
    fn new(piece: char, colour: char) -> King {
        King {
            data: Data { piece, colour },
            moved: false,
        }
    }
}

#[derive(Clone)]
struct Empty {
    data: Data,
}

impl Piece for Empty {
    fn is_valid(
        &self,
        _working_index: usize,
        _target_index: usize,
        _turn: char,
        _board: &[Box<dyn Piece>],
    ) -> bool {
        false
    }

    fn is_colour(&self, _colour: char) -> bool {
        false
    }

    fn get_colour(&self) -> char {
        ' '
    }

    fn get_type(&self) -> char {
        ' '
    }

    fn box_clone(&self) -> Box<dyn Piece> {
        Box::new(self.clone())
    }
}

impl Empty {
    fn new() -> Empty {
        Empty {
            data: Data {
                piece: ' ',
                colour: ' ',
            },
        }
    }
}

pub fn new_piece(piece: char, colour: char) -> Box<dyn Piece> {
    match piece {
        'P' => Box::new(Pawn::new(piece, colour)),
        'R' => Box::new(Rook::new(piece, colour)),
        'N' => Box::new(Knight::new(piece, colour)),
        'B' => Box::new(Bishop::new(piece, colour)),
        'Q' => Box::new(Queen::new(piece, colour)),
        'K' => Box::new(King::new(piece, colour)),
        ' ' => Box::new(Empty::new()),
        _ => panic!("Invalid piece"),
    }
}
// Comment
