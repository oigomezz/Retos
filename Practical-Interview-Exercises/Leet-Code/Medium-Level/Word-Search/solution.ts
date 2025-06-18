function exist(board: string[][], word: string): boolean {
  const rows: number = board.length;
  const cols: number = board[0].length;
  const visited: Set<string> = new Set();

  const dfs = (r: number, c: number, k: number): boolean => {
    if (k === word.length) return true;
    if (
      r < 0 ||
      r >= rows ||
      c < 0 ||
      c >= cols ||
      visited.has(`${r},${c}`) ||
      board[r][c] !== word[k]
    )
      return false;

    visited.add(`${r},${c}`);
    const res: boolean =
      dfs(r + 1, c, k + 1) ||
      dfs(r - 1, c, k + 1) ||
      dfs(r, c + 1, k + 1) ||
      dfs(r, c - 1, k + 1);
    visited.delete(`${r},${c}`);
    return res;
  };

  const count: { [key: string]: number } = {};
  for (const c of word) count[c] = (count[c] || 0) + 1;

  if (count[word[0]] > count[word[word.length - 1]])
    word = word.split("").reverse().join("");

  for (let r = 0; r < rows; r++)
    for (let c = 0; c < cols; c++) if (dfs(r, c, 0)) return true;

  return false;
}
