function generateMatrix(n: number): number[][] {
  const matrix: number[][] = Array.from({ length: n }, () => Array(n).fill(0));
  let left = 0,
    right = n - 1,
    top = 0,
    bottom = n - 1;

  let num = 1;
  while (left <= right && top <= bottom) {
    // Fill top row
    for (let i = left; i <= right; i++) matrix[top][i] = num++;
    top++;

    // Fill right column
    for (let i = top; i <= bottom; i++) matrix[i][right] = num++;
    right--;

    // Fill bottom row
    if (top <= bottom) {
      for (let i = right; i >= left; i--) matrix[bottom][i] = num++;
      bottom--;
    }

    // Fill left column
    if (left <= right) {
      for (let i = bottom; i >= top; i--) matrix[i][left] = num++;
      left++;
    }
  }

  return matrix;
}
