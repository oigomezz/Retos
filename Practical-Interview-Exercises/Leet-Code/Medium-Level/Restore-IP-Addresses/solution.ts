function restoreIpAddresses(s: string): string[] {
  const result: string[] = [];

  function isValid(segment: string): boolean {
    if (segment.length > 1 && segment[0] === "0") return false;
    const num = Number(segment);
    return num >= 0 && num <= 255;
  }

  function backtrack(start: number, current: string[]): void {
    if (current.length === 4) {
      if (start === s.length) result.push(current.join("."));
      return;
    }

    for (let len = 1; len <= 3; len++) {
      if (start + len <= s.length) {
        const segment = s.slice(start, start + len);
        if (isValid(segment)) {
          current.push(segment);
          backtrack(start + len, current);
          current.pop();
        }
      }
    }
  }

  backtrack(0, []);
  return result;
}
