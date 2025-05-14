function removeElement(nums: number[], val: number): number {
  let slow = 0;
  for (const element of nums) {
    if (element !== val) {
      nums[slow] = element;
      slow++;
    }
  }
  return slow;
}
