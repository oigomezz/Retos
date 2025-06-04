# [Crazy Matrix][link]

Praveen went crazy yesterday and created an arbitrary matrix consisting of 0, 1 or 2. There was no rule observed in forming this matrix. But then he made up some rules himself.

If there are adjacent 1's, they are said to be connected. Similarly, if there are adjacent 2's, they are said to be connected. Here adjacent means all the surrounding positions along with the diagonal positions.

Now given a matrix of 0, 1 or 2, do your computation according to the following rules:

1. If there is a path from any position in top row to any position in bottom row consisting only of 1, then print 1.
2. If there is a path from any position in first column to any position in last column consisting only of 2, then print 2.
3. If both Rule 1 & Rule 2 are true, print AMBIGUOUS.
4. If none of Rule 1, Rule 2 or Rule 3 satisfies, print 0.

## Input format

- First line of input contains a positive integer N, the size of matrix.
- Then N line follows, each containing N integers which are either 0, 1 or 2.

## Output format

Print a single line containing the output according to the rule mentioned. Clearly, the output can only be 0, 1, 2 or AMBIGUOUS.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/crazy-matrix/
