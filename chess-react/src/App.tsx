import './App.css';
import Chessboard from './components/chessboard/chessboard';

function App() {
    // const defaultFen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
    return (
    <div id="app">
      <Chessboard fen='r2qnrk1/3nbppp/p2pb3/4p1P1/1p2PP2/1N2B3/PPPQN2P/2KR1B1R b - - 0 14'/>
    </div>
  );
}

export default App;
