# [Sprinklers][link]

There are N sprinklers in a field. Each sprinkler has some range up to where it can sprinkle water.

All the sprinklers are on the X-axis at coordinates (X1,0), (X2,0), ..., (Xn,0) and their respective ranges are R1, R2, ..., Rn meaning that the i-th sprinkler can sprinkle water from [Xi - Ri, Xi + Ri] inclusive.

There is a big wall at 0 meaning that the water can not go another side irrespective of range.

You are asked Q queries and in the i-th query, you will be given an integer K. Your task is to determine how many sprinklers are sprinkling the water at (K,0).

Assume, there is no sprinkler at (0,0) and there is no query that has K = 0.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first line of each test case contains two integers N and Q denoting the number of sprinklers and number of queries.
- The second line of each test case contains N space-separated integers denoting the X-coordinates of the sprinklers.
- The third line of each test case contains N space-separated integers denoting the range of the sprinklers.
- Next Q line of each test case contains an integer K for the query.

## Output format

For each test case, print Q lines denoting the number of sprinklers that sprinkle water at the position in the i-th query.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/sprinklers-7153515e/
