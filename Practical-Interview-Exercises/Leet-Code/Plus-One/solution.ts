function plusOne(digits: number[]): number[] {
  let carry = 1;
  for (let i = digits.length - 1; i >= 0; i--) {
    digits[i] += carry;
    if (digits[i] === 10) {
      digits[i] = 0;
    } else {
      carry = 0;
      break;
    }
  }

  if (carry) digits.unshift(1);

  return digits;
}
