function subsets(nums: number[]): number[][] {
  const res: number[][] = [];
  const subset: number[] = [];

  const createSubset = (i: number): void => {
    if (i === nums.length) {
      res.push([...subset]);
      return;
    }

    subset.push(nums[i]);
    createSubset(i + 1);

    subset.pop();
    createSubset(i + 1);
  };

  createSubset(0);
  return res;
}
