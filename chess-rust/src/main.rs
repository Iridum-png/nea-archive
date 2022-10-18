use board::Board;
use std::{fs::File, io};
mod board;

fn process<'a>(coordinate: (&'a str, &'a str)) -> (i32, i32) {
    let mut coord1: i32 = coordinate.1.parse().unwrap();
    let mut coord2: i32 = coordinate.0.parse().unwrap();
    return (coord1 - 1, coord2 - 97);
}

fn reset_turn(board: &Board) {
    board::Board::print_board(&board);
    turn(board);
}

fn turn(board: &board::Board) -> bool {
    let valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

    // Take the input for starting position
    println!("Enter start position (e.g. a1): ");
    let mut start = String::new();
    io::stdin()
        .read_line(&mut start)
        .expect("Error: unable to read user input");
    // Check if the first character of start is in valid_letters
    if !valid_letters.contains(&start.chars().nth(0).unwrap()) {
        println!("Error: invalid start position");
        reset_turn(board);
    }
    // Convert the input into useable coordinates
    let start_pos = process(start.split_at(0));

    // Take the input for starting position
    println!("Enter end position (e.g. h8): ");
    let mut end = String::new();
    io::stdin()
        .read_line(&mut end)
        .expect("Error: unable to read user input");
    // Check if the first character of start is in valid_letters
    if !valid_letters.contains(&end.chars().nth(0).unwrap()) {
        println!("Error: invalid start position");
        reset_turn(board);
    }
    // Convert the input into useable coordinates
    let end_pos = process(end.split_at(0));

    board::Board::r#move(&board, start_pos, end_pos);
    return board::Board::is_won(&board);
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
