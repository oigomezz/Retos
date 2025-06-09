function totalNQueens(n: number): number {
  let count = 0;
  const board: string[] = Array.from({ length: n }, () => ".".repeat(n));

  const isSafe = (row: number, col: number): boolean => {
    for (let i = 0; i < row; i++) {
      if (board[i][col] === "Q") return false;
      if (col - (row - i) >= 0 && board[i][col - (row - i)] === "Q")
        return false;
      if (col + (row - i) < n && board[i][col + (row - i)] === "Q")
        return false;
    }
    return true;
  };

  const solve = (row: number): void => {
    if (row === n) {
      count++;
      return;
    }
    for (let col = 0; col < n; col++) {
      if (isSafe(row, col)) {
        board[row] =
          board[row].substring(0, col) + "Q" + board[row].substring(col + 1);
        solve(row + 1);
        board[row] =
          board[row].substring(0, col) + "." + board[row].substring(col + 1);
      }
    }
  };

  solve(0);
  return count;
}
