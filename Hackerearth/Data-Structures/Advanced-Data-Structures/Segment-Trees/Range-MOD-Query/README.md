# [Range MOD Query][link]

You are given a binary string, s, and you have to answer q queries in order.

A binary string is a string consisting of only 0's and 1's.

There are two types of queries:

- 1 i : Flip the character at position i i.e 0 becomes 1, and 1 becomes 0. Each modification affects the subsequent queries i.e the queries are dependent.
- 2 l r : Print the decimal value of the binary substring formed by indices in some range [l,r]. As the value could be very large, compute it modulo 10⁹ + 7.

## Input format

- The first line of the input contains two integers, n and q - denoting the number of characters in the string s and the number of queries.
- The second line of the input contains the string s - the string contains only 0's or 1's
- The next q lines of the input contain two types of queries:
  - 1 i - denoting a type 1 query and the index to be flipped.
  - 2 l r - denoting a type 2 query and the indices to find the decimal value modulo 10⁹ + 7.

## Output format

For each of the type 2 queries, output an integer denoting the decimal value of the binary representation of the queried range modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/bob-and-string-easy/
