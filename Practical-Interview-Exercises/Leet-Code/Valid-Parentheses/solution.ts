function isValid(s: string): boolean {
  const stack: string[] = [];
  const map: { [key: string]: string } = {
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (const char of s) {
    if (map[char]) stack.push(map[char]);
    else if (stack.length === 0 || stack.pop() !== char) return false;
  }

  return stack.length === 0;
}
