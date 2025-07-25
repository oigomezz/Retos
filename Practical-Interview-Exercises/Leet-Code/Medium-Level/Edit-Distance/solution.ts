function minDistance(word1: string, word2: string): number {
  const m: number = word1.length;
  const n: number = word2.length;

  const dp: number[][] = Array.from({ length: m + 1 }, () =>
    Array(n + 1).fill(0)
  );

  for (let i: number = 0; i <= m; i++) dp[i][0] = i;
  for (let j: number = 0; j <= n; j++) dp[0][j] = j;

  for (let i: number = 1; i <= m; i++) {
    for (let j: number = 1; j <= n; j++) {
      if (word1[i - 1] === word2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
      else
        dp[i][j] = Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1;
    }
  }

  return dp[m][n];
}
