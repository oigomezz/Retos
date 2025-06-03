function findSubstring(s: string, words: string[]): number[] {
  const result: number[] = [];
  if (!s || words.length === 0) return result;

  const wordLength = words[0].length;
  const totalWordsLength = wordLength * words.length;
  const wordCount: { [key: string]: number } = {};

  for (const word of words) {
    wordCount[word] = (wordCount[word] || 0) + 1;
  }

  for (let i = 0; i <= s.length - totalWordsLength; i++) {
    const seen: { [key: string]: number } = {};
    let j = 0;
    while (j < words.length) {
      const word = s.substring(i + j * wordLength, i + (j + 1) * wordLength);
      if (!wordCount[word]) break;

      seen[word] = (seen[word] || 0) + 1;
      if (seen[word] > wordCount[word]) break;

      j++;
    }

    if (j === words.length) result.push(i);
  }

  return result;
}
