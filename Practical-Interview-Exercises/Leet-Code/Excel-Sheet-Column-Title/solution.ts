function convertToTitle(columnNumber: number): string {
  let title = "";
  while (columnNumber > 0) {
    columnNumber--; // Decrement to make it 0-indexed
    const remainder = columnNumber % 26;
    title = String.fromCharCode(65 + remainder) + title;
    columnNumber = Math.floor(columnNumber / 26);
  }
  return title;
}
