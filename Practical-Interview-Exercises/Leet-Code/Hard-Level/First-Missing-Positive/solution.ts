function firstMissingPositive(nums: number[]): number {
  const n = nums.length;

  // Step 1: Replace negative numbers and zeros with n + 1
  for (let i = 0; i < n; i++) {
    if (nums[i] <= 0 || nums[i] > n) nums[i] = n + 1;
  }

  // Step 2: Use the index to mark the presence of numbers
  for (let i = 0; i < n; i++) {
    const num = Math.abs(nums[i]);
    if (num <= n) nums[num - 1] = -Math.abs(nums[num - 1]);
  }

  // Step 3: Find the first missing positive
  for (let i = 0; i < n; i++) {
    if (nums[i] > 0) return i + 1;
  }

  return n + 1;
}
