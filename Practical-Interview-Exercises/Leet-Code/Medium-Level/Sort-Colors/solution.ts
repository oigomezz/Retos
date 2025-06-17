/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
  let red: number = 0;
  let white: number = 0;
  let blue: number = nums.length - 1;

  while (white <= blue) {
    if (nums[white] === 0) {
      [nums[white], nums[red]] = [nums[red], nums[white]];
      red++;
      white++;
    } else if (nums[white] === 1) {
      white++;
    } else {
      [nums[white], nums[blue]] = [nums[blue], nums[white]];
      blue--;
    }
  }
}
