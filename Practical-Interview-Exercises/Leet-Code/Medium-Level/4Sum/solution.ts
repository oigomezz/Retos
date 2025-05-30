function fourSum(nums: number[], target: number): number[][] {
  const result: number[][] = [];
  const n = nums.length;

  if (n < 4) return result;

  nums.sort((a, b) => a - b);

  for (let i = 0; i < n - 3; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue; // Skip duplicates for the first number

    for (let j = i + 1; j < n - 2; j++) {
      if (j > i + 1 && nums[j] === nums[j - 1]) continue; // Skip duplicates for the second number

      let left = j + 1;
      let right = n - 1;

      while (left < right) {
        const sum = nums[i] + nums[j] + nums[left] + nums[right];

        if (sum === target) {
          result.push([nums[i], nums[j], nums[left], nums[right]]);

          while (left < right && nums[left] === nums[left + 1]) left++; // Skip duplicates for the third number
          while (left < right && nums[right] === nums[right - 1]) right--; // Skip duplicates for the fourth number

          left++;
          right--;
        } else if (sum < target) left++;
        else right--;
      }
    }
  }

  return result;
}
