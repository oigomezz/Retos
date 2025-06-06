function trap(height: number[]): number {
  if (height.length === 0) return 0;

  let left = 0;
  let right = height.length - 1;
  let leftMax = height[left];
  let rightMax = height[right];
  let waterTrapped = 0;

  while (left < right) {
    if (leftMax < rightMax) {
      left++;
      leftMax = Math.max(leftMax, height[left]);
      waterTrapped += leftMax - height[left];
    } else {
      right--;
      rightMax = Math.max(rightMax, height[right]);
      waterTrapped += rightMax - height[right];
    }
  }

  return waterTrapped;
}
