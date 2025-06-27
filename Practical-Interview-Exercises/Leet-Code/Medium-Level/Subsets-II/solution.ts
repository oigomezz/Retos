function subsetsWithDup(nums: number[]): number[][] {
  const res: number[][] = [];
  const backtrack = (start: number, path: number[]) => {
    res.push([...path]);
    for (let i = start; i < nums.length; i++) {
      if (i > start && nums[i] === nums[i - 1]) continue; // Skip duplicates
      path.push(nums[i]);
      backtrack(i + 1, path);
      path.pop();
    }
  };
  nums.sort((a, b) => a - b);
  backtrack(0, []);
  return res;
}
