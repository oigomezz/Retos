function numDecodings(s: string): number {
  if (s.startsWith("0")) return 0;

  const n: number = s.length;
  const dp: number[] = new Array(n + 1).fill(0);
  dp[0] = dp[1] = 1;

  for (let i: number = 2; i <= n; i++) {
    const one: number = parseInt(s[i - 1]);
    const two: number = parseInt(s.substring(i - 2, i));

    if (1 <= one && one <= 9) dp[i] += dp[i - 1];
    if (10 <= two && two <= 26) dp[i] += dp[i - 2];
  }

  return dp[n];
}
