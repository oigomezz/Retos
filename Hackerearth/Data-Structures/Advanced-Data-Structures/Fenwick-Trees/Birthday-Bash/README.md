# Birthday Bash

Emma planned to buy a string S consisting of lowercase English characters of size N as a gift for her friend Ava on her birthday. Ava had Q other friends who also wanted to contribute but were not happy with the string. So all Q of her friends decide to do either of the two operations:

- 1 x: Give an index x and ask Emma to reverse the string from index x to N-x-1.
- 2 x: Give an index x and ask Emma to change the character at index x to the alphabetically next character. For example, if the character was a, it would become b (assume that a is alphabetically next to z).

All of this was too much for Emma to handle alone. So she asked you to help her find the final string after doing all the operations.

**Note:** Assume 0-based indexing.

## Input format

- The first line of input contains an integer T, denoting the number of test cases.
- The first line of each test case contains two integers, N and Q, denoting the size of the string and the number of friends of Ava respectively.
- The following line contains a string of size N.
- The next Q line contains two integers and is one of two types:
  - 1 x denoting that Emma needs to reverse the string from index x to N-x-1 (it is guaranteed that x will be less than N-x-1).
  - 2 x denoting that Emma needs to change the x-th character to alphabetically next character.

## Output format

For each test case, print a string of size N denoting the final string.
