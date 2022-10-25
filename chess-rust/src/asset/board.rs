// Use piece
use crate::asset::piece::new_piece;
use crate::asset::piece::Piece;

pub struct Board {
    pub board: Vec<Box<dyn Piece>>,
    pub turn: char,
    pub move_count: u8,
}

impl Board {
    pub fn load_from_fen(&mut self, fen: String) -> Vec<i32> {
        // Parse FEN string
        let fen_board = fen
            .split_whitespace()
            .nth(0)
            .unwrap()
            .chars()
            .rev()
            .collect::<String>();
        let board_arr = fen_board.split("/").collect::<Vec<&str>>();
        for row in board_arr {
            for piece in row.chars() {
                if piece.is_numeric() {
                    for _ in 0..piece.to_digit(10).unwrap() {
                        self.board.push(new_piece(' ', ' '));
                    }
                } else {
                    let colour = if piece.is_uppercase() { 'w' } else { 'b' };
                    let working = new_piece(piece, colour);
                    self.board.push(working);
                }
            }
        }
        return (0..64).collect::<Vec<i32>>();
    }

    pub fn print_board(&self) {
        println!(" +--+--+--+--+--+--+--+--+");
        let mut row_num = 8;
        for i in (0..8).rev() {
            print!("{}|", row_num);
            for j in 0..8 {
                let working = &self.board[(i * 8) + j];
                print!("{}{}|", working.get_colour(), working.get_type());
            }
            println!("\n +--+--+--+--+--+--+--+--+");
            row_num -= 1;
        }
        println!(
            "  a  b  c  d  e  f  g  h\t{}'s turn",
            self.turn.to_uppercase()
        );
    }

    pub fn r#move(&mut self, start: (i32, i32), end: (i32, i32)) {
        let working_index = (start.0 * 8 + start.1) as usize;
        let working: &Box<dyn Piece> = &self.board[working_index];
        let target_index = (end.0 * 8 + end.1) as usize;

        // Check if move is valid
        if working.is_valid(working_index, target_index, self.turn, &self.board) {
            self.board = move_me(self.board, working_index, target_index);
            self.board[working_index] = new_piece(' ', ' ');
            self.turn = if self.turn == 'w' { 'b' } else { 'w' };
            if self.turn == 'w' {
                self.move_count += 1;
            }
        } else {
            println!("Invalid move");
        }
    }

    pub fn is_won(&self) -> bool {
        false
    }
}

fn move_me(mut arr: [Box<dyn Piece>], old_index: usize, new_index: usize) -> Vec<Box<dyn Piece>> {
    if old_index < new_index {
        arr[old_index..=new_index].rotate_left(1);
    } else {
        arr[new_index..=old_index].rotate_right(1);
    }
    arr
}
