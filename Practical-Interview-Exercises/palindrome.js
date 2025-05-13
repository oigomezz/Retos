function palindrome(str) {
  const str_no_spaces = str.replace(/\s/g, "");
  const pal = str_no_spaces.split("").reverse().join();
  return str_no_spaces === pal;
}
