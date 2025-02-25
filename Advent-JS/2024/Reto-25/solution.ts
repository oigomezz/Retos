function execute(code: string): number {
  let pos = 0;
  let val = 0;
  let loopIndex = 0;
  const delta: Record<string, number> = {
    "-": -1,
    "+": +1,
  };
  const pairs = {
    "{": "}",
    "[": "]",
  };

  while (pos < code.length) {
    let char = code[pos];
    if (char in pairs) {
      if (val === 0) {
        let pair = pairs[char];
        pos += code.substring(pos).indexOf(pair);
      } else if (char === "[") loopIndex = pos;
    } else if (char === "]") {
      if (val !== 0) pos = loopIndex;
    } else val += delta[char] || 0;
    pos += 1;
  }

  return val;
}

export { execute };
