function uniquePaths(m: number, n: number): number {
  let aboveRow = Array(n).fill(1);

  for (let row = 1; row < m; row++) {
    let currentRow = Array(n).fill(1);
    for (let col = 1; col < n; col++)
      currentRow[col] = currentRow[col - 1] + aboveRow[col];

    aboveRow = currentRow;
  }

  return aboveRow[n - 1];
}
