import './chessboard.css';
import Tile from '../tile/tile';

interface Props {
    fen: string;
}

interface Piece {
    image: string;
    x: number;
    y: number;
}

const horizontalAxis = ["a", "b", "c", "d", "e", "f", "g", "h"];
const verticalAxis = ["1", "2", "3", "4", "5", "6", "7", "8"]; // Array isn't needed here but is used for the sake of consistency and potential for modularity

function FenToPos({fen}: Props) {
    // Convert fen string to board position
    console.log(fen);
}

export default function Chessboard() {
    let board = [];
    
    for (let j = verticalAxis.length - 1; j >= 0; j--) {
        for (let i = 0; i < horizontalAxis.length; i++) { // Renders from top left to bottom right (a8 - h1)
            const number = j + i + 2;
            board.push(<Tile number={number}/>);
        }
    }

    return <div id="chessboard">{board}</div>
}