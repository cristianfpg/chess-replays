const getMoveFromTurn = (pgnMatch: string, turn: number): string => {
  const moves = pgnMatch
    .replace(/\d+\./g, '') 
    .trim()
    .split(/\s+/);

  const selectedMoves = moves.slice(0, turn);

  let result = '';
  for (let i = 0; i < selectedMoves.length; i++) {
    const moveNumber = Math.floor(i / 2) + 1;

    if (i % 2 === 0) result += `${moveNumber}. `;
    result += selectedMoves[i] + ' ';
  }

  return result.trim();
}

export default getMoveFromTurn