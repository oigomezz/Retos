function multiply(num1: string, num2: string): string {
  if (num1 === "0" || num2 === "0") return "0";

  const m = num1.length,
    n = num2.length;
  const result = Array(m + n).fill(0);

  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      const mul = Number(num1[i]) * Number(num2[j]);
      const sum = mul + result[i + j + 1];

      result[i + j + 1] = sum % 10;
      result[i + j] += Math.floor(sum / 10);
    }
  }

  // Convert result array to string
  return result.join("").replace(/^0+/, "") ?? "0";
}
