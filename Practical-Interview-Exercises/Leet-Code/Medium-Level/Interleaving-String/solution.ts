function isInterleave(s1: string, s2: string, s3: string): boolean {
  const m: number = s1.length,
    n: number = s2.length;
  if (m + n !== s3.length) return false;

  const dp: boolean[] = Array(n + 1).fill(false);
  dp[0] = true;

  for (let j: number = 1; j <= n; j++) {
    dp[j] = dp[j - 1] && s2[j - 1] === s3[j - 1];
  }

  for (let i: number = 1; i <= m; i++) {
    dp[0] = dp[0] && s1[i - 1] === s3[i - 1];
    for (let j: number = 1; j <= n; j++) {
      dp[j] =
        (dp[j] && s1[i - 1] === s3[i + j - 1]) ||
        (dp[j - 1] && s2[j - 1] === s3[i + j - 1]);
    }
  }

  return dp[n];
}
