const myAtoi = (s: string): number => {
  let i: number = 0,
    n: number = s.length,
    sign: number = 1,
    result: number = 0;

  // Skip whitespaces
  while (i < n && s[i] === " ") i++;

  // Sign detection
  if (i < n && (s[i] === "+" || s[i] === "-")) {
    sign = s[i] === "-" ? -1 : 1;
    i++;
  }

  // Parse digits
  while (i < n && s[i] >= "0" && s[i] <= "9") {
    result = result * 10 + (s.charCodeAt(i) - "0".charCodeAt(0));
    if (result * sign > 2 ** 31 - 1) return 2 ** 31 - 1;
    if (result * sign < -(2 ** 31)) return -(2 ** 31);
    i++;
  }

  return result * sign;
};
