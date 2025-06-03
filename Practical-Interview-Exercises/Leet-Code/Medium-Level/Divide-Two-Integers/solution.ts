function divide(dividend: number, divisor: number): number {
  const INT_MIN: number = -(2 ** 31);
  const INT_MAX: number = 2 ** 31 - 1;
  if (dividend === INT_MIN && divisor === -1) return INT_MAX;
  if (dividend === INT_MIN && divisor === 1) return INT_MIN;

  const isNegative: boolean = dividend < 0 !== divisor < 0;

  let a: number = Math.abs(dividend);
  let b: number = Math.abs(divisor);
  let quotient: number = 0;

  let i: number = 31;
  while (a >= b) {
    if (i < 0) break;
    if (a >>> i >= b) {
      quotient += 1 << i;
      a -= b << i;
    }
    i--;
  }

  return isNegative ? -quotient : quotient;
}
