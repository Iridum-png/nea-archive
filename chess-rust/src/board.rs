pub struct Board {
    pub board: Vec<i32>,
    pub turn: char,
    pub move_count: u8,
}

impl Board {
    pub fn load_from_fen(&self, fen: String) -> Vec<i32> {
        // Parse FEN string
        let binding = fen
            .split_whitespace()
            .nth(0)
            .unwrap()
            .chars()
            .rev()
            .collect::<String>();
        // Return vec of all numbers 0 to 63
        (0..64).collect::<Vec<i32>>()
    }

    pub fn print_board(&self) {
        println!(" +--+--+--+--+--+--+--+--+");
        let mut row_num = 8;
        for i in (0..8).rev() {
            print!("{}|", row_num);
            for j in 0..8 {
                println!("{:?}", self.board);
                let current = self.board[i * 8 + j];
                match current {
                    0 => print!("  |"),
                    _ => print!("{}|", current),
                }
            }
            println!("\n +--+--+--+--+--+--+--+--+");
            row_num -= 1;
        }
        println!("  a  b  c  d  e  f  g  h\t{}'s turn", self.turn);
    }
}
