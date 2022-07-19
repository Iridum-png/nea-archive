use core::fmt::Debug;
use std::fmt::Display;

struct Piece {
    colour: char,
    x: u8,
    y: u8,
    prevx: u8,
    prevy: u8,
    piece: char,
}
struct Board {
    order: Vec<char>,
    board: Vec<Vec<Piece>>,
}

impl Debug for Piece {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}{}", self.colour, self.piece)
        // write!(f, "{} {}", self.x, self.y)
    }
}
impl Display for Piece {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}{}", self.colour, self.piece)
    }
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
            self.board[0].push(Piece {
                colour: 'W',
                x: 0,
                y: i as u8,
                prevx: 0,
                prevy: i as u8,
                piece: order[i],
            });
        }
        for i in 0..8 {
            self.board[1].push(Piece {
                colour: 'W',
                x: 1,
                y: i as u8,
                prevx: 0,
                prevy: i as u8,
                piece: 'P',
            });
        }
        for i in 2..6 {
            for j in 0..8 {
                self.board[i].push(Piece {
                    colour: '#',
                    x: j as u8,
                    y: i as u8,
                    prevx: i as u8,
                    prevy: j as u8,
                    piece: '#',
                });
            }
        }
        for i in 0..8 {
            self.board[6].push(Piece {
                colour: 'B',
                x: 6,
                y: i as u8,
                prevx: 0,
                prevy: i as u8,
                piece: 'P',
            });
        }
        for i in 0..8 {
            self.board[7].push(Piece {
                colour: 'B',
                x: 7,
                y: i as u8,
                prevx: 0,
                prevy: i as u8,
                piece: order[i],
            });
        }
    }

    pub fn output(&self, row: usize) {
        for i in 0..8 {
            print!("{}", self.board[row][i]);
        }
        println!();
    }
}

fn output(game: Board) {
    print!("\x1B[2J");
    for i in 0..8 {
        println!("+----+----+----+----+----+----+----+----+");
        print!("{}|", 8 - i);
        for piece in game.board[i] {}
    }
}

fn main() {
    let mut game = Board {
        order: Vec::new(),
        board: Vec::new(),
    };
    game.init();
    output(game);
}
