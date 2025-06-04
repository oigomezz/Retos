function solveSudoku(board: string[][]): void {
  const isValid = (row: number, col: number, num: string): boolean => {
    for (let i = 0; i < 9; i++) {
      if (board[row][i] === num || board[i][col] === num) return false;
      const boxRow = 3 * Math.floor(row / 3) + Math.floor(i / 3);
      const boxCol = 3 * Math.floor(col / 3) + (i % 3);
      if (board[boxRow][boxCol] === num) return false;
    }
    return true;
  };

  const solve = (): boolean => {
    for (let row = 0; row < 9; row++) {
      for (let col = 0; col < 9; col++) {
        if (board[row][col] === ".") {
          for (let num = 1; num <= 9; num++) {
            const strNum = String(num);
            if (isValid(row, col, strNum)) {
              board[row][col] = strNum;
              if (solve()) return true;
              board[row][col] = "."; // backtrack
            }
          }
          return false; // no valid number found
        }
      }
    }
    return true; // solved
  };

  solve();
}
