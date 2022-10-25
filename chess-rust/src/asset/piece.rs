pub enum Piece {
    Pawn(Data, bool),
    Rook(Data, bool),
    Knight(Data),
    Bishop(Data),
    Queen(Data),
    King(Data, bool),
    Empty(Data),
}

impl Piece {
    fn is_valid(&self, start: usize, end: usize, turn: char, board: &Vec<Piece>) -> bool {
        self.is_valid(start, end, turn, board)
    }

    fn get_type(&self) -> char {
        self.get_type()
    }

    fn get_colour(&self) -> char {
        self.get_colour()
    }

    pub fn new_piece(piece: char, colour: char) -> Piece {
        match piece {
            'P' => Pawn::new(colour),
            'R' => Rook::new(colour),
            'N' => Knight::new(colour),
            'B' => Bishop::new(colour),
            'Q' => Queen::new(colour),
            'K' => King::new(colour),
            ' ' => Empty::new(),
            _ => panic!("Invalid piece"),
        }
    }
}

#[derive(Clone)]
struct Data {
    piece: char,
    colour: char,
}

struct Pawn {
    data: Data,
    moved: bool,
}

impl Pawn {
    fn new(colour: char) -> Piece {
        Piece::Pawn(Data { piece: 'P', colour }, false)
    }

    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        _board: &[Piece],
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
        self.data.colour
    }
}

struct Rook {
    data: Data,
    moved: bool,
}

impl Rook {
    fn new(colour: char) -> Piece {
        Piece::Rook(Data { piece: 'R', colour }, false)
    }

    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        board: &[Piece],
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
        self.data.colour
    }
}

struct Knight {
    data: Data,
}

impl Knight {
    fn new(colour: char) -> Piece {
        Piece::Knight(Data { piece: 'N', colour })
    }

    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        _board: &[Piece],
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
        self.data.colour
    }
}

struct Bishop {
    data: Data,
}

impl Bishop {
    fn new(colour: char) -> Piece {
        Piece::Bishop(Data { piece: 'B', colour })
    }

    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        board: &[Piece],
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
        self.data.colour
    }
}

struct Queen {
    data: Data,
}

impl Queen {
    fn new(colour: char) -> Piece {
        Piece::Queen(Data { piece: 'Q', colour })
    }

    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        board: &[Piece],
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
        self.data.colour
    }
}

struct King {
    data: Data,
    moved: bool,
}

impl King {
    fn new(colour: char) -> Piece {
        Piece::King(Data { piece: 'K', colour }, false)
    }

    fn is_valid(
        &self,
        working_index: usize,
        target_index: usize,
        turn: char,
        _board: &[Piece],
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
        self.data.colour
    }
}

struct Empty {
    data: Data,
}

impl Empty {
    fn new() -> Piece {
        Piece::Empty(Data {
            piece: ' ',
            colour: ' ',
        })
    }
}
