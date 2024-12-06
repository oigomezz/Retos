function getIndexsForPalindrome(word) {
  if (word === word.split("").reverse().join("")) return [];
  let newWord = [];
  for (let i = 0; i < word.length; i++) {
    for (let j = 0; j < word.length; j++) {
      if (i === j) continue;
      newWord = word.split("");
      const aux = newWord[i];
      newWord[i] = newWord[j];
      newWord[j] = aux;
      const newBaseWord = newWord.join("");
      if (newWord.reverse().join("") === newBaseWord) return [i, j];
    }
  }
  return null;
}

console.log(getIndexsForPalindrome("anna")); // []
console.log(getIndexsForPalindrome("abab")); // [0, 1]
console.log(getIndexsForPalindrome("abac")); // null
console.log(getIndexsForPalindrome("aaaaaaaa")); // []
console.log(getIndexsForPalindrome("aaababa")); // [1, 3]
console.log(getIndexsForPalindrome("caababa")); // null
