function ladderLength(
  beginWord: string,
  endWord: string,
  wordList: string[]
): number {
  const wordSet = new Set<string>(wordList);
  if (!wordSet.has(endWord)) return 0;

  let beginSet = new Set<string>([beginWord]);
  let endSet = new Set<string>([endWord]);
  const visited = new Set<string>();
  let steps = 1;

  const aCharCode = "a".charCodeAt(0);

  while (beginSet.size && endSet.size) {
    if (beginSet.size > endSet.size) {
      [beginSet, endSet] = [endSet, beginSet];
    }

    const nextSet = new Set<string>();

    for (const word of beginSet) {
      for (let i = 0; i < word.length; i++) {
        for (let c = 0; c < 26; c++) {
          const ch = String.fromCharCode(aCharCode + c);
          if (ch === word[i]) continue;

          const newWord = word.slice(0, i) + ch + word.slice(i + 1);
          if (endSet.has(newWord)) return steps + 1;

          if (wordSet.has(newWord) && !visited.has(newWord)) {
            visited.add(newWord);
            nextSet.add(newWord);
          }
        }
      }
    }

    beginSet = nextSet;
    steps++;
  }

  return 0;
}
