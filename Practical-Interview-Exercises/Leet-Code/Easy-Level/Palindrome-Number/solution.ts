function isPalindrome(x: number): boolean {
  const str = x.toString();
  const reversed = str.split("").reverse().join("");
  return str === reversed;
}