function longestPalindrome(s: string): string {
  let longest = "";
  for (let i = 0; i < s.length; i++) {
    // Check for odd-length palindromes
    let odd = expandAroundCenter(s, i, i);
    if (odd.length > longest.length) longest = odd;

    // Check for even-length palindromes
    let even = expandAroundCenter(s, i, i + 1);
    if (even.length > longest.length) longest = even;
  }
  return longest;
}

function expandAroundCenter(s: string, left: number, right: number): string {
  while (left >= 0 && right < s.length && s[left] === s[right]) {
    left--;
    right++;
  }
  return s.slice(left + 1, right);
}
