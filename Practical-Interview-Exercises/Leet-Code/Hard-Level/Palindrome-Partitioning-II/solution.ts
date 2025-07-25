function minCut(s: string): number {
  const n: number = s.length;
  const dp: number[] = Array(n)
    .fill(0)
    .map((_, i) => i);

  const expansion = (l: number, r: number): void => {
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      const cut: number = l === 0 ? 0 : dp[l - 1] + 1;
      dp[r] = Math.min(dp[r], cut);
      l--;
      r++;
    }
  };

  for (let i = 0; i < n; i++) {
    expansion(i, i);
    expansion(i - 1, i);
  }

  return dp[n - 1];
}
