struct Board {
    order: Vec<char>,
    board: Vec<Vec<Piece>>,
}

struct Piece {
    colour: char,
    x: u8,
    y: u8,
    prevx: u8,
    prevy: u8,
    piece: char,
}

impl Board {
    pub fn init(&mut self) {
        let order = vec!['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'];
        for elem in order.iter() {
            self.order.push(*elem);
        }
        for _ in 0..8 {
            self.board.push(Vec::new())
        }
        for i in 0..8 {
            self.board[i].push(Piece {
                colour: 'W',
                x: 0,
                y: i as u8,
                prevx: 0,
                prevy: i as u8,
                piece: order[i],
            });
        }
    }
}

fn main() {
    let mut game = Board {
        order: Vec::new(),
        board: Vec::new(),
    };
    game.init();
}
