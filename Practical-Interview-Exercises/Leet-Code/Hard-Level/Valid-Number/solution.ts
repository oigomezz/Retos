function isNumber(s: string): boolean {
  const regex = /^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$/;
  return regex.test(s);
}
