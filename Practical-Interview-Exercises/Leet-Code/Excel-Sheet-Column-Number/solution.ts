function titleToNumber(columnTitle: string): number {
  let columnNumber = 0;
  for (let i = 0; i < columnTitle.length; i++) {
    const charCode = columnTitle.charCodeAt(i) - "A".charCodeAt(0) + 1;
    columnNumber = columnNumber * 26 + charCode;
  }
  return columnNumber;
}
