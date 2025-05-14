function lengthOfLastWord(s: string): number {
  let length = 0;
  let foundLetter = false;

  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === " ") {
      if (foundLetter) break;
    } else {
      foundLetter = true;
      length++;
    }
  }

  return length;
}
