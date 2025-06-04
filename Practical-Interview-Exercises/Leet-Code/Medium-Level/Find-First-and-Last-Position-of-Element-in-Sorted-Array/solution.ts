function searchRange(nums: number[], target: number): number[] {
  const findLeft = (nums: number[], target: number): number => {
    let left = 0,
      right = nums.length - 1;
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (nums[mid] < target) left = mid + 1;
      else right = mid - 1;
    }
    return left < nums.length && nums[left] === target ? left : -1;
  };

  const findRight = (nums: number[], target: number): number => {
    let left = 0,
      right = nums.length - 1;
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (nums[mid] <= target) left = mid + 1;
      else right = mid - 1;
    }
    return right >= 0 && nums[right] === target ? right : -1;
  };

  const leftIndex = findLeft(nums, target);
  const rightIndex = findRight(nums, target);

  return [leftIndex, rightIndex];
}
