function nextPermutation(nums: number[]): void {
  const n = nums.length;
  let i = n - 2;

  // Find the first decreasing element from the end
  while (i >= 0 && nums[i] >= nums[i + 1]) {
    i--;
  }

  if (i >= 0) {
    // Find the element just larger than nums[i] to swap with
    let j = n - 1;
    while (j > i && nums[j] <= nums[i]) {
      j--;
    }
    [nums[i], nums[j]] = [nums[j], nums[i]];
  }

  // Reverse the elements after the original position of i
  let left = i + 1;
  let right = n - 1;
  while (left < right) {
    [nums[left], nums[right]] = [nums[right], nums[left]];
    left++;
    right--;
  }
}
