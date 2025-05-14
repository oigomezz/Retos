function addBinary(a: string, b: string): string {
  let carry = 0;
  let result = "";

  const maxLength = Math.max(a.length, b.length);
  a = a.padStart(maxLength, "0");
  b = b.padStart(maxLength, "0");

  for (let i = maxLength - 1; i >= 0; i--) {
    const sum = parseInt(a[i]) + parseInt(b[i]) + carry;
    if (sum >= 2) {
      carry = 1;
      result = (sum % 2).toString() + result;
    } else {
      carry = 0;
      result = sum.toString() + result;
    }
  }

  if (carry) result = "1" + result;

  return result;
}
