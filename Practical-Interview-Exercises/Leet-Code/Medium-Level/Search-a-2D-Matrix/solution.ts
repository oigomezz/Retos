function searchMatrix(matrix: number[][], target: number): boolean {
  const [rows, cols]: [number, number] = [matrix.length, matrix[0].length];
  let [top, bot]: [number, number] = [0, rows - 1];

  while (top <= bot) {
    const row: number = Math.floor((top + bot) / 2);
    if (target > matrix[row][cols - 1]) top = row + 1;
    else if (target < matrix[row][0]) bot = row - 1;
    else break;
  }

  if (!(top <= bot)) return false;

  const row: number = Math.floor((top + bot) / 2);
  let [left, right]: [number, number] = [0, cols - 1];

  while (left <= right) {
    const mid: number = Math.floor((left + right) / 2);

    if (target > matrix[row][mid]) left = mid + 1;
    else if (target < matrix[row][mid]) right = mid - 1;
    else if (target === matrix[row][mid]) return true;
  }

  return false;
}
