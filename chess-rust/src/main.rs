use board::Board;
use std::{fs::File, io};
mod board;

fn process<'a>(coordinate: (&'a str, &'a str)) -> (&'a [u8], &'a [u8]) {
    return (coordinate.1.as_bytes(), coordinate.0.as_bytes());
}

fn reset_turn(board: &Board) {
    board::Board::print_board(&board);
    turn(board);
}

fn turn(board: &board::Board) -> bool {
    let valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
    let mut start;
    io::stdin()
        .read_line(&mut start)
        .expect("error: unable to read user input");
}

fn main() {
    let _log = File::create("log.log");

    let board = self::board::Board {
        board: vec![],
        turn: 'w',
        move_count: 0,
    };

    board::Board::load_from_fen(
        &board,
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1".to_string(),
    );

    let mut won = turn(&board);

    while !won {
        self::board::Board::print_board(&board);
        won = turn(&board);
    }
}
