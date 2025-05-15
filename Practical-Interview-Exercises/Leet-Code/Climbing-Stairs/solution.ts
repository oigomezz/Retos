function climbStairs(n: number): number {
  if (n <= 0) return 0;
  if (n === 1) return 1;
  let prev = 1;
  let curr = 1;
  for (let i = 2; i <= n; i++) {
    const temp = curr;
    curr += prev;
    prev = temp;
  }
  return curr;
}
