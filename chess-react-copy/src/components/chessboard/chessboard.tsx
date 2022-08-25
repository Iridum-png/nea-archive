import './chessboard.css';
import Tile from '../tile/tile';
import React, { useRef } from 'react';

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

let activePiece: HTMLElement | null = null; 

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
    const chessboardRef = useRef<HTMLDivElement>(null);

    function grabPiece(e: React.MouseEvent) {
        const element = e.target as HTMLImageElement;
        if (element.classList.contains('chess-piece')) {
            const x = e.clientX;
            const y = e.clientY;

            element.style.position = 'absolute';
            element.style.left = `${x-40}px`;
            element.style.top = `${y-40}px`;
            
            activePiece = element;
        }
    }

    function movePiece(e: React.MouseEvent) {
        const chessboard = chessboardRef.current;
        if (activePiece && chessboard) {
            const minX = chessboard.offsetLeft-41;
            const minY = chessboard.offsetTop-40;
            const x = e.clientX;
            const y = e.clientY;

            activePiece.style.position = 'absolute';
            activePiece.style.left = `${Math.max(minX,x-40)}px`;
            activePiece.style.top = `${y-40}px`;
        }
    }

    function dropPiece(e: React.MouseEvent) {
        if (activePiece) {
            activePiece = null;
        }
    }
    let board = [];
    
    fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
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
                image: boardArray[i],
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
            board.push(<Tile image={image} number={number} />);
        }
    }

    return (
        <div
            onMouseMove={(e) => movePiece(e)}
            onMouseDown={(e) => grabPiece(e)}
            onMouseUp={(e) => dropPiece(e)}
            id="chessboard"
            ref={chessboardRef}>
            {board}
        </div>
    );
}