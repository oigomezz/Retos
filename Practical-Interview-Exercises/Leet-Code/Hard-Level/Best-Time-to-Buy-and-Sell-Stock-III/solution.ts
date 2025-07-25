function maxProfit(prices: number[]): number {
  const n: number = prices.length;
  if (n === 0) return 0;
  const dp: number[][] = Array.from({ length: 3 }, () => Array(n).fill(0));

  // we iterate over number of transactions: 1 and 2
  for (let k = 1; k <= 2; k++) {
    let maxDiff: number = 0 - prices[0]; // max of (dp[k-1][j] - prices[j]) for j < i

    for (let i = 1; i < n; i++) {
      dp[k][i] = Math.max(dp[k][i - 1], prices[i] + maxDiff);
      maxDiff = Math.max(maxDiff, dp[k - 1][i] - prices[i]);
    }
  }

  return dp[2][n - 1];
}
