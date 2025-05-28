function getRow(rowIndex: number): number[] {
  const row: number[] = [1];
  for (let i = 1; i <= rowIndex; i++) {
    row[i] = (row[i - 1] * (rowIndex - i + 1)) / i;
  }
  return row;
}
