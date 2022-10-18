pub struct Board {
    pub board: Vec<i32>,
    pub turn: char,
    pub move_count: u8,
}

impl Board {
    pub fn printBoard(board: Board) {
        let mut value = 0;

        while value != 64 {
            println!("{}, {}", board.board[value], value);
            value += 1;
        }
    }
}
