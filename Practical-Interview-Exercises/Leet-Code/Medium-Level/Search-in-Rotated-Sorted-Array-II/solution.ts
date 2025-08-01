function search(nums: number[], target: number): boolean {
  let left: number = 0;
  let right: number = nums.length - 1;

  while (left <= right) {
    let mid: number = Math.floor((left + right) / 2);

    if (nums[mid] === target) return true;

    if (nums[mid] === nums[left]) {
      left++;
      continue;
    }

    if (nums[left] <= nums[mid]) {
      if (nums[left] <= target && target < nums[mid]) right = mid - 1;
      else left = mid + 1;
    } else {
      if (nums[mid] < target && target <= nums[right]) left = mid + 1;
      else right = mid - 1;
    }
  }

  return false;
}
