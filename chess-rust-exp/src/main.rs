mod asset;

// ######################################
// ##                                  ##
// ##    Driver code for chess game    ##
// ##                                  ##
// ######################################

fn input(message: &str) -> String {
    println!("{}", message);
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    println!("{:?}", input);
    return input.trim().to_string();
}

fn turn(mut input: &str, board: &asset::Board) -> bool {
    // todo!("Implement turn");
    // let from = input.next().unwrap();
    // let to = input.next().unwrap();
    // let from = asset::Tile::new(from);
    // let to = asset::Tile::new(to);
    // board.move_piece(from, to);
    false
}

fn main() {
    // Setup the board
    let mut board = asset::Board::new();
    let fen = input("Enter a FEN string to load the board from:");
    board.load_from_fen(Some(&fen));
    let mut won = false;
    while !won {
        board = board.print_board();
        let mut input = input("Enter move (eg a1 h8): ");
        won = turn(&input, &board);
    }
}
