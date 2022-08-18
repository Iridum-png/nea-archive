import './chessboard.css';
import Tile from '../tile/tile';

interface Props {
    fen: string
}

interface Piece {
    image?: string
    x: number
    y: number
}

const pieces: Piece[] = [];

const horizontalAxis = ["a", "b", "c", "d", "e", "f", "g", "h"];
const verticalAxis = ["1", "2", "3", "4", "5", "6", "7", "8"]; 

function FenToPos(fen: string) {
    const fenArr = fen.split('');
    const fenReference: {[key: string]: string} = {r: 'rook_b', R: 'rook_w', n: 'knight_b', N: 'knight_w', b: 'bishop_b', B: 'bishop_w', q: 'queen_b', Q: 'queen_w', k: 'king_b', K: 'king_w', p: 'pawn_b', P: 'pawn_w' };
    let temp1: string[] = [];
    let temp2: string[][] = [];
    let boardArray: string[] = [];
    fenArr.forEach(f => {
        if (isNumeric(f)) {
            for (let i = 0; i < parseInt(f); i++) {
                temp1.push(' ');
            }
        } else {
            temp1.push(`assets/images/${fenReference[f]}.png`);
        }
    })
    // very ugly code, but it works
    // reverses array in chunks of 8 in order to render it properly
    // TIDY UP NEEDED
    for (let i = 0; i < 8; i++) {
        temp2.push(temp1.slice(64 - (i + 1) * 8, 64 - i * 8));
    }
    temp2.forEach(t => {
        t.forEach(e => {
            boardArray.push(e);
        })
    })
    return boardArray;
}

function isNumeric(str: any) {
    return !isNaN(str);
}   

export default function Chessboard({ fen }: Props) {
    let board = [];
    
    fen = '8/5k2/3p4/1p1Pp2p/pP2Pp1P/P4P1K/8/8 b';
    const boardArray = FenToPos(fen.substring(0, fen.indexOf(' ')).replaceAll('/', '')); // Takes only the needed part to calculate the position of the board
    
    for (let i = 0; i < 64; i++) {
        if (boardArray[i] === ' ') {
            pieces.push({
                image: undefined, 
                x: i % 8,
                y: Math.floor(i / 8)
            });
        } else {
            pieces.push({
            image:  boardArray[i], 
            x: i % 8,
            y: Math.floor(i / 8)
        });
        }
    }

    for (let j = verticalAxis.length - 1; j >= 0; j--) {
        for (let i = 0; i < horizontalAxis.length; i++) {
            const number = j + i + 2;
            let image = undefined;

            pieces.forEach(p => {
                if (p.x === i && p.y === j) {
                    image = p.image;
                }
            })
            board.push(<Tile image={image} number={number}/>);
        }
    }

    return <div id="chessboard">{board}</div>
}