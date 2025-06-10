function minWindow(s: string, t: string): string {
  const charCount = new Map<string, number>();
  for (const char of t) charCount.set(char, (charCount.get(char) ?? 0) + 1);

  let left = 0;
  let right = 0;
  let minLength = Infinity;
  let minWindow = "";
  const requiredChars = charCount.size;
  let formedChars = 0;
  const windowCounts = new Map<string, number>();

  while (right < s.length) {
    const rightChar = s[right];
    windowCounts.set(rightChar, (windowCounts.get(rightChar) ?? 0) + 1);

    if (
      charCount.has(rightChar) &&
      windowCounts.get(rightChar) === charCount.get(rightChar)
    )
      formedChars++;

    while (left <= right && formedChars === requiredChars) {
      const currentWindow = s.slice(left, right + 1);
      if (currentWindow.length < minLength) {
        minLength = currentWindow.length;
        minWindow = currentWindow;
      }

      const leftChar = s[left];
      windowCounts.set(leftChar, windowCounts.get(leftChar)! - 1);
      if (
        charCount.has(leftChar) &&
        (windowCounts.get(leftChar) ?? 0) < charCount.get(leftChar)!
      )
        formedChars--;
      left++;
    }
    right++;
  }

  return minWindow;
}
