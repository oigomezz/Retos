function permute(nums: number[]): number[][] {
  const result: number[][] = [];
  const backtrack = (path: number[], used: boolean[]) => {
    if (path.length === nums.length) {
      result.push([...path]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.push(nums[i]);
      backtrack(path, used);
      path.pop();
      used[i] = false;
    }
  };
  backtrack([], Array(nums.length).fill(false));
  return result;
}
