function mySqrt(x: number): number {
  if (x < 0) throw new Error("Input must be a non-negative number");

  let left = 0;
  let right = x;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);

    if (mid * mid === x) return mid;
    else if (mid * mid < x) left = mid + 1;
    else right = mid - 1;
  }

  return right;
}
