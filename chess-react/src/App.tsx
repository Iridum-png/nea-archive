import './App.css';
import Chessboard from './components/chessboard/chessboard';

function App() {
  return (
    <div id="app">
      <Chessboard fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'/>
    </div>
  );
}

export default App;
