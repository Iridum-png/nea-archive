pub enum Piece {
    Pawn(char, bool),
    Rook(char, bool),
    Knight(char),
    Bishop(char),
    Queen(char),
    King(char, bool),
    Empty(char),
}

impl Piece {
    pub fn is_valid(
        piece: &Piece,
        start: usize,
        end: usize,
        turn: char,
        board: &Vec<Piece>,
    ) -> bool {
        match piece {
            Piece::Pawn(..) => is_valid_pawn(start, end, turn),
            Piece::Rook(..) => is_valid_rook(start, end, board),
            Piece::Knight(..) => is_valid_knight(start, end),
            Piece::Bishop(..) => is_valid_bishop(start, end, board),
            Piece::Queen(..) => is_valid_queen(start, end, board),
            Piece::King(..) => is_valid_king(start, end),
            Piece::Empty(..) => false,
        }
    }

    pub fn get_type(piece: &Piece) -> char {
        match piece {
            Piece::Pawn(..) => 'P',
            Piece::Rook(..) => 'R',
            Piece::Knight(..) => 'N',
            Piece::Bishop(..) => 'B',
            Piece::Queen(..) => 'Q',
            Piece::King(..) => 'K',
            Piece::Empty(..) => ' ',
        }
    }

    pub fn get_colour(piece: &Piece) -> char {
        match piece {
            Piece::Pawn(colour, _) => *colour,
            Piece::Rook(colour, _) => *colour,
            Piece::Knight(colour) => *colour,
            Piece::Bishop(colour) => *colour,
            Piece::Queen(colour) => *colour,
            Piece::King(colour, _) => *colour,
            Piece::Empty(colour) => *colour,
        }
    }

    pub fn new_piece(piece: char, colour: char) -> Piece {
        match piece {
            'P' => Piece::Pawn(colour, false),
            'R' => Piece::Rook(colour, false),
            'N' => Piece::Knight(colour),
            'B' => Piece::Bishop(colour),
            'Q' => Piece::Queen(colour),
            'K' => Piece::King(colour, false),
            ' ' => Piece::Empty(colour),
            _ => panic!("Invalid piece"),
        }
    }
}

fn is_valid_pawn(start: usize, end: usize, turn: char) -> bool {
    let start_row = start / 8;
    let start_col = start % 8;
    let end_row = end / 8;
    let end_col = end % 8;

    // Check if move is valid
    if turn == 'W' {
        if start_row == 6 {
            if end_row == 4 && start_col == end_col {
                return true;
            }
        }
        if end_row == start_row - 1 && start_col == end_col {
            return true;
        }
    } else {
        if start_row == 1 {
            if end_row == 3 && start_col == end_col {
                return true;
            }
        }
        if end_row == start_row + 1 && start_col == end_col {
            return true;
        }
    }

    // Allow for diagonal capture
    if turn == 'W' {
        if (end_row == start_row - 1 && (end_col == start_col + 1 || end_col == start_col - 1) && ) {
            return true;
        }
    } else {
        if (end_row == start_row + 1 && (end_col == start_col + 1 || end_col == start_col - 1) && ) {
            return true;
        }
    }
    false
}

fn is_valid_rook(start: usize, end: usize, board: &Vec<Piece>) -> bool {
    let start_row = start / 8;
    let start_col = start % 8;
    let end_row = end / 8;
    let end_col = end % 8;

    // Check if move is valid
    if !start_row == end_row || start_col == end_col {
        return false;
    }

    // Check if piece is in way
    if start_row == end_row {
        if start_col < end_col {
            for i in start_col + 1..end_col {
                if Piece::get_type(&board[start_row * 8 + i]) != ' ' {
                    return false;
                }
            }
        } else {
            for i in end_col + 1..start_col {
                if Piece::get_type(&board[start_row * 8 + i]) != ' ' {
                    return false;
                }
            }
        }
    } else {
        if start_row < end_row {
            for i in start_row + 1..end_row {
                if Piece::get_type(&board[i * 8 + start_col]) != ' ' {
                    return false;
                }
            }
        } else {
            for i in end_row + 1..start_row {
                if Piece::get_type(&board[i * 8 + start_col]) != ' ' {
                    return false;
                }
            }
        }
    }
    return true;
}

fn is_valid_knight(start: usize, end: usize) -> bool {
    let start_row = start / 8;
    let start_col = start % 8;
    let end_row = end / 8;
    let end_col = end % 8;

    // Check if move is valid
    if start_row.abs_diff(end_row) == 2 && start_col.abs_diff(end_col) == 1 {
        return true;
    }
    if start_row.abs_diff(end_row) == 1 && start_col.abs_diff(end_col) == 2 {
        return true;
    }
    return false;
}

fn is_valid_bishop(start: usize, end: usize, board: &Vec<Piece>) -> bool {
    let start_row = start / 8;
    let start_col = start % 8;
    let end_row = end / 8;
    let end_col = end % 8;

    // Check if move is valid
    if start_row.abs_diff(end_row) != start_col.abs_diff(end_col) {
        return false;
    }

    // Check if piece is in way
    if start_row < end_row {
        if start_col < end_col {
            for i in 1..end_row - start_row {
                if Piece::get_type(&board[(start_row + i) * 8 + start_col + i]) != ' ' {
                    return false;
                }
            }
        } else {
            for i in 1..end_row - start_row {
                if Piece::get_type(&board[(start_row + i) * 8 + start_col - i]) != ' ' {
                    return false;
                }
            }
        }
    } else {
        if start_col < end_col {
            for i in 1..start_row - end_row {
                if Piece::get_type(&board[(start_row - i) * 8 + start_col + i]) != ' ' {
                    return false;
                }
            }
        } else {
            for i in 1..start_row - end_row {
                if Piece::get_type(&board[(start_row - i) * 8 + start_col - i]) != ' ' {
                    return false;
                }
            }
        }
    }
    return true;
}

fn is_valid_queen(start: usize, end: usize, board: &Vec<Piece>) -> bool {
    is_valid_rook(start, end, board) || is_valid_bishop(start, end, board)
}

fn is_valid_king(start: usize, end: usize) -> bool {
    let start_row = start / 8;
    let start_col = start % 8;
    let end_row = end / 8;
    let end_col = end % 8;

    // Check if move is valid
    if start_row.abs_diff(end_row) <= 1 && start_col.abs_diff(end_col) <= 1 {
        return true;
    }
    return false;
}
