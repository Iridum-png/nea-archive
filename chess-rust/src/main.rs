use std::fs::File;
mod board;

fn process<'a>(coordinate: (&'a str, &'a str)) -> (&'a [u8], &'a [u8]) {
    return (coordinate.1.as_bytes(), coordinate.0.as_bytes());
}

fn turn(&board: &board::Board) -> bool {
    false
}

fn main() {
    let _log = File::create("log.log");

    let board = self::board::Board {
        board: vec![0],
        turn: 'w',
        move_count: 0,
    };
    let mut won = turn(&board);

    while !won {
        self::board::Board::printBoard(board);
        won = turn(board);
    }
}
