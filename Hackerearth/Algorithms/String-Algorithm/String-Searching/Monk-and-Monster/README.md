# [Monk And Monster][link]

Monster is troubling the Monk. Monk is given a task to completely traverse the string P . Monster owns a string Q.

Monk cannot traverse the string P if there is an index i in P such that Q is a prefix of the sub-string of P starting at 'i' until Monster allows him to do so.Monk is rich so he pays the monster whenever he finds such an index and Monster asks him for money.

Monster takes different amounts of money for allowing a jump at index i. Thus, you are given 2 strings P and Q and a cost array. The size of the array is N which is same as length of P .Determine the maximum amount Monster can get from Monk. By jump it means that if Monk jumps at index 'i' then he reaches index 'i+|Q|'.

## Note

- N is guaranteed to be equal to P
- Monk cannot jump at any index until Q is a prefix of substring at index i of P.
- If Monk doesn’t jump at any particular index he doesn’t pay anything.
- Monster may(i.e it is not necessary) ask for money from Monk if Q is a prefix of substring at index i of P. He may also let him go for free if he thinks he can gain more in future.

## Input format

- First line contains number of testcases T.
- Each testcase consists of four lines:
  - First line consists of string P.
  - Second line consists of string Q.(Both strings consist of lowercase English characters only).
  - Next line contains an integer N.
  - Next line contains an integer cost array.

## Output format

Output the maximum amount Monster can get.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/string-searching/practice-problems/algorithm/monk-and-monster-1acbb78c/
