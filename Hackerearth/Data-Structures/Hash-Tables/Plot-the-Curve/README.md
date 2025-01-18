# [Plot the Curve][link]

You are given with integers a,b,c,d,m. These represent the modular equation of a curve y² mod m = (ax³ + bx² + cx + d) mod m.

Also, you are provided with an array A of size N. Now, your task is to find the number of pairs in the array that satisfy the given modular equation.

If (Ai,Aj) is a pair then A²j mod m = (aA³i + bA²i + cAi + d) mod m.

Since the answer could be very large output it modulo 10⁹ + 7.

**Note:** A pair is counted different from some other pair if either Ai of the two pairs is different or Aj of the two pairs is different. Also for the convenience of calculations, we may count (Ai,Ai) as a valid pair if it satisfies given constraints.

## Input format

- First line of the input contains number of test cases T.
- First line for each test case consists of 5 space-separated integers a,b,c,d,m, corresponding to modular equation given.
- Next line contains a single integer N.
- Next line contains N space-separated integers corresponding to values of array A.

## Output format

For each test case, output a single line corresponding to number of valid pairs in the array mod 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/lets-plot-this-47a575ed/
