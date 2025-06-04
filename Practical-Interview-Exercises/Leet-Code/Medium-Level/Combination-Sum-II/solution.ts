function combinationSum2(candidates: number[], target: number): number[][] {
  const result: number[][] = [];
  candidates.sort((a, b) => a - b); // Sort to handle duplicates

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
      // Skip duplicates
      if (i > start && candidates[i] === candidates[i - 1]) continue;

      currentCombination.push(candidates[i]);
      backtrack(i + 1, currentCombination, currentSum + candidates[i]);
      currentCombination.pop();
    }
  }

  backtrack(0, [], 0);
  return result;
}
