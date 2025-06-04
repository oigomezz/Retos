function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function backtrack(
    start: number,
    currentCombination: number[],
    currentSum: number
  ) {
    if (currentSum === target) {
      result.push([...currentCombination]);
      return;
    }
    if (currentSum > target) return;

    for (let i = start; i < candidates.length; i++) {
      currentCombination.push(candidates[i]);
      backtrack(i, currentCombination, currentSum + candidates[i]);
      currentCombination.pop();
    }
  }

  backtrack(0, [], 0);
  return result;
}
