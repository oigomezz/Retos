function getPermutation(n: number, k: number): string {
  const factorials: number[] = [1];
  for (let i = 1; i <= n; i++) factorials[i] = factorials[i - 1] * i;

  const nums: number[] = Array.from({ length: n }, (_, i) => i + 1);
  let kAdjusted = k - 1; // Convert to zero-based index
  let result: string[] = [];

  for (let i = n; i > 0; i--) {
    const index = Math.floor(kAdjusted / factorials[i - 1]);
    result.push(nums[index].toString());
    nums.splice(index, 1);
    kAdjusted %= factorials[i - 1];
  }

  return result.join("");
}
