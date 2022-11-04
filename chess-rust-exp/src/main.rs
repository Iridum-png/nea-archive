mod asset;

// ######################################
// ##                                  ##
// ##    Driver code for chess game    ##
// ##                                  ##
// ######################################

fn main() {
    let mut board = asset::Board::new();
    board.load_from_fen(None);
    board.print_board();
}
