use ascii_converter::string_to_decimals;
use asset::{board, Board};
use std::io;
mod asset;

fn process<'a>(coordinate: (&'a str, &'a str)) -> (i32, i32) {
    let coord1: i32 = coordinate.1.trim().parse().unwrap();
    let coord2: i32 =
        string_to_decimals(&coordinate.0.to_string().to_ascii_lowercase()).unwrap()[0] as i32;
    return (coord1 - 1, coord2 - 97);
}

fn reset_turn(board: &mut Board) {
    board::Board::print_board(&board);
    turn(board);
}

fn turn(board: &mut Board) -> bool {
    let valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

    // Take the input for starting position
    println!("Enter start position (e.g. a1): ");
    let start = input();
    // Check if the first character of start is in valid_letters
    if !valid_letters.contains(&start.chars().nth(0).unwrap()) {
        println!("Error: invalid start position");
        reset_turn(board);
    }
    // Convert the input into useable coordinates
    let start_pos = process(start.strip_suffix("\n").unwrap().split_at(1));

    // Take the input for starting position
    println!("Enter end position (e.g. h8): ");
    let end = input();
    // Check if the first character of start is in valid_letters
    if !valid_letters.contains(&end.chars().nth(0).unwrap()) {
        println!("Error: invalid start position");
        reset_turn(board);
    }
    // Convert the input into useable coordinates
    let end_pos = process(end.strip_suffix("\n").unwrap().split_at(1));

    board::Board::r#move(board, start_pos, end_pos);
    return board::Board::is_won(board);
}

fn input() -> String {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Error: unable to read user input");
    return input;
}

fn main() {
    // let log = File::create("log.log");

    let mut board = self::board::Board {
        board: vec![],
        turn: 'W',
        move_count: 0,
    };
    println!(
        "Enter FEN string (Default: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1): "
    );
    board::Board::load_from_fen(&mut board, input());
    let mut won = false;

    while !won {
        self::board::Board::print_board(&board);
        won = turn(&mut board);
    }
}
