// Use the Tile struct from tile
use crate::asset::tile::Tile;

pub struct Board {
    tiles: Vec<Option<Tile>>,
}

impl Board {
    pub fn new() -> Board {
        Board {
            tiles: std::iter::repeat_with(|| None).take(64).collect::<Vec<_>>(),
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
            if c.is_digit(10) {
                i += c.to_digit(10).unwrap();
            } else {
                self.tiles[i] = Tile::new(i % 2 == 0, c);
                i += 1;
            }
        }
    }

    pub fn print(&self) {
        for i in 0..64 {
            if i % 8 == 0 {
                println!();
            }
            print!("{}", self.tiles[i].to_string());
        }
        println!();
    }
}
