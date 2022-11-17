mod asset;

// ######################################
// ##                                  ##
// ##    Driver code for chess game    ##
// ##                                  ##
// ######################################

<<<<<<< HEAD
fn fen_input() -> String {
    println!("Enter custom FEN string if you wish: ");
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();

    // Check if input is valid
    if input.trim().is_empty() {
        return String::from("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    } else {
        return input.trim().to_string();
    }
}

fn turn(board: &mut asset::Board) -> u8 {
    board.print_board();
    return board.is_checkmate();
}

fn main() {
    let mut board = asset::Board::new();
    board.load_from_fen(Some(&fen_input()));
    board.print_board();
    let mut won = 0;

    while won == 0 {
        won = turn(&mut board);
    }
    if won == 1 {
        println!("White wins!");
    } else if won == 2 {
        println!("Black wins!");
    } else if won == 3 {
        println!("Draw!");
    } else {
        panic!("Invalid win status!");
=======
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
>>>>>>> 6cc83f690286307d73d7403a8291c230f798d339
    }
}
