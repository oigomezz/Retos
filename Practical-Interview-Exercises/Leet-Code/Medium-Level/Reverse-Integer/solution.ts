function reverse(x: number): number {
  const isNegative = x < 0;
  const reversed = parseInt(x.toString().split("").reverse().join(""), 10);
  if (isNegative) return reversed > 0x7fffffff ? 0 : -reversed;

  return reversed > 0x7fffffff ? 0 : reversed;
}
