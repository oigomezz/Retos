function minimumTotal(triangle: number[][]): number {
  const row: number = triangle.length;
  const memo: number[] = [...triangle[row - 1]];

  for (let r: number = row - 2; r >= 0; r--) {
    for (let c: number = 0; c <= r; c++) {
      memo[c] = Math.min(memo[c], memo[c + 1]) + triangle[r][c];
    }
  }

  return memo[0];
}
