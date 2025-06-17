/**
 Do not return anything, modify matrix in-place instead.
 */
function setZeroes(matrix: number[][]): void {
  let col: number[] = new Array(matrix.length).fill(0),
    row: number[] = new Array(matrix[0].length).fill(0);

  for (let i: number = 0; i < matrix.length; i++) {
    for (let j: number = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] === 0) {
        row[i] = 1;
        col[j] = 1;
      }
    }
  }

  for (let i: number = 0; i < matrix.length; i++)
    for (let j: number = 0; j < matrix[i].length; j++)
      if (row[i] === 1 || col[j] === 1) matrix[i][j] = 0;
}
