function combine(n: number, k: number): number[][] {
  const res: number[][] = [];
  const comb: number[] = [];

  function backtrack(start: number): void {
    if (comb.length === k) {
      res.push([...comb]);
      return;
    }

    for (let num = start; num <= n; num++) {
      comb.push(num);
      backtrack(num + 1);
      comb.pop();
    }
  }

  backtrack(1);
  return res;
}
