import React from 'react';
import './chessboard.css';

const horizontalAxis = ["a", "b", "c", "d", "e", "f", "g", "h"];
const verticalAxis = ["1", "2", "3", "4", "5", "6", "7", "8"]; // Array isn't needed here but is used for the sake of consistency and potential for modularity

export default function Chessboard() {
    let board = [];
    
    for (let j = verticalAxis.length - 1; j >= 0; j--) {
        for (let i = 0; i < horizontalAxis.length; i++) { // Renders from top left to bottom right
            const number = j + i + 2;

            if (number % 2 == 0) {
                board.push(<div className="tile black-tile"></div>);
            } else {
                board.push(<div className="tile white-tile"></div>);
            }
        }
    }

    return <div id="chessboard">{board}</div>
}