# [Boolean Expressions][link]

Roy is intrigued by the fact that the evaluated value of boolean expressions can easily vary depending upon the order of evaluation !

For instance, consider the example:

Expression: 1 xor 1 and 0

We can have following two interpretations:

1. ((1 xor 1) and 0) => (0 and 0) => 0
2. (1 xor (1 and 0)) => (1 xor 0) => 1

Now, he is further interested into finding the number of possible different parenthesizations such that the result of computation is res.

## Input format

- The first line of input file contains two space-separated strings. The first string denotes the literals of our boolean expression S, the second string denotes the operators.
- The next line denotes an integer q, i.e. the number of queries to follow.
- Each of the next q lines contain two space separated integers l and r and a string res, which is either true or false.

## Output format

For each query. output in a new line, the number of ways in which the boolean expression of substring [l,r] can be parenthesized so that it evaluates to res. As the output can be very large, please print the answer modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/boolean-expressions-2/
