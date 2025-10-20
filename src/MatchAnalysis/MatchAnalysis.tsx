import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';
import { useEffect, useState } from 'react';
import getMoveFromTurn from './utilities/getMoveFromTurn';
import pgnMatch from './services/getMatch';

const MatchAnalysis = () => {
  const [turn, setTurn] = useState<number>(0);
  const [position, setPosition] = useState<string>('');

  const handleTurn = (e: React.ChangeEvent<HTMLInputElement>): void => {
    setTurn(parseInt(e.target.value));
  }

  useEffect(() => {
    const chess = new Chess();
    chess.loadPgn(getMoveFromTurn(pgnMatch, turn));
    setPosition(chess.fen());
  }, [turn]);

  return(
    <>
      <input type="number" onChange={handleTurn}/>
      <Chessboard
        options={{
          position: position
        }} />
    </> 
  )
}

export default MatchAnalysis;