# [Greatest common divisor][link]

You are given array A. There are 4 types of operations associated with it:

- 1 l r x, for each i ∈ [l, r] replace ai with the value of x.
- 2 l r x, for each i ∈ [l, r] replace ai with the value of the gcd(ai, x) function.
- 3 l r, print the value of max ai, l ≤ i ≤ r.
- 4 l r, print the value of al + al+1 + ... + ar.

A greatest common divisor (gcd(a, b)) of two positive integers a and b is equal to the biggest integer d such that both integers a and b are divisible by d.

## Input format

- The first line contains two integers n, m (1 ≤ n, m ≤ 10⁵) - the number of array elements and the number of queries.
- The second line contains n positive integers a1, a2, ..., an - initial state of the array.(1 ≤ max Ai ≤ 10⁹, 1 ≤ i ≤ n)
- Next m lines contain the description of the queries, one per line. Queries are formatted the same way as in the problem statement above.
- It is guaranteed that 1 ≤ l ≤ r ≤ n and 1 ≤ x ≤ 10⁹.

## Output format

For each third and fourth query type, print the answer for this query in a separate line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/cool-gcd-789acd8e/
