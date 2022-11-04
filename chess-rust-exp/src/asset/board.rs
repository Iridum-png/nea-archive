// Use the Tile struct from tile
use crate::asset::tile::Tile;

pub struct Board {
    tiles: Vec<Option<Tile>>,
    turn: char,
}

impl Board {
    pub fn new() -> Board {
        Board {
            tiles: std::iter::repeat_with(|| None).take(64).collect::<Vec<_>>(),
            turn: 'W',
        }
    }

    pub fn load_from_fen(&mut self, fen: Option<&str>) {
        let fen = fen
            .unwrap_or("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
            .split_whitespace()
            .nth(0)
            .unwrap()
            .chars()
            .rev()
            .collect::<String>();
        println!("FEN: {}", fen);
        let mut i = 0;
        for c in fen.chars() {
            if i >= 64 {
                break;
            }
            if c.is_digit(10) {
                for _ in 0..c.to_digit(10).unwrap() {
                    self.tiles[i] = Some(Tile::new(i % 2 == 0, ' '));
                    i += 1;
                }
            } else {
                self.tiles[i as usize] = Some(Tile::new(i % 2 == 0, c));
                i += 1;
            }
        }
        self.turn = fen
            .split_whitespace()
            .nth(1)
            .unwrap()
            .chars()
            .nth(0)
            .unwrap();
    }

    pub fn print_board(&self) {
        println!(" +--+--+--+--+--+--+--+--+");
        let mut row_num = 8;
        for i in (0..8).rev() {
            print!("{}|", row_num);
            for j in 0..8 {
                let tile = self.tiles[(i * 8) + j].as_ref();
                match tile {
                    Some(tile) => print!("{}{}|", tile.get_colour(), tile.get_piece()),
                    None => print!("  |"),
                };
            }
            println!("\n +--+--+--+--+--+--+--+--+");
            row_num -= 1;
        }
        println!("  a  b  c  d  e  f  g  h\t{}'s turn", self.turn);
    }
}
