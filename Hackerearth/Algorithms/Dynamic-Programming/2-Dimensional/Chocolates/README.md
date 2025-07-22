# [Chocolates][link]

Simon has bought a box of chocolate and has brought them to Amanda's house. There is a random number on each chocolate. They decided to play a game with them.

They arranged them randomly in a row. They each start from one end of the row (Simon starts from left and Amanda from right). They can only move towards each other, and in each step, they can move at most k chocolate.

More specifically Simon can go from the i-th place to one of i+1, i+2, ..., i+k and Amanda can go from i-th place to i-1, i-2, ..., i-k.

They can only eat the chocolate they are on if their number is the same. The game ends if they can eat any chocolate. Their goal is to eat the last chocolate together.

Determine if Simon and Amanda can eat the last chocolate together (that is, they both finish in the same place).

Note that in the initial state, they are on the first and n-th place but they did not eat chocolates yet. So, if the number of the first and n-th place chocolate differs, the game ends and they would not reach each other. Also, at each moment, they both have to move simultaneously, that is, one cannot stay at a place while another one is moving because if one stays at the n-th place, there is not any chocolate to eat anymore.

## Input format

- The first line of input contains integers n and k denoting the length of the array and the maximum length of their steps respectively.
- The second line contains n integers denoting the elements of array A.

## Output format

Print "YES" if they can eat the last chocolate together and "NO" if they cannot.

**Note:** The letters in the words "YES" and "NO" should be uppercase.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/simon-amanda-and-the-last-chocolate-9db82979/
