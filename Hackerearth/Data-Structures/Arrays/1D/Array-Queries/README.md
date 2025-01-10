# [Array queries][link]

You are given 2 arrays A and B of length N and M respectively.

Given Q queries in form of array queries, you need to output Q + 1 integers. The initial value of F(A, B) and the values after each query. The value of F(A, B) can be very large so, output the values modulo 998244353.

Complete the array_queries function provided in the editor. This function takes the following 6 parameters and returns a vector/array denoting the values of F(A, B) for all queries:

- N: Represents an integer denoting the length of array A
- M: Represents an integer denoting the length of array B
- A: Represents the integer array A
- B: Represents the integer array B
- Q: Represents an integer denoting the number of queries
- queries: Represents a 2D array/vector denoting queries of the type "1 i j" or "2 i j" or "3 i j". Therefore, the size of the queries array is Q\*3.

## Input format

- The first line contains a single integer T, which denotes the number of test cases. T also specifies the number of times you have to run the array_queries function on a different set of inputs.
- For each test case:
  - The first line contains an integer N denoting the length of the array A.
  - The second line contains an integer M denoting the length of the array B.
  - The third line contains N space-separated integers denoting array A.
  - The fourth line contains M space-separated integers denoting array B.
  - The fifth line contains an integer Q denoting the number of queries.
  - The next Q lines follow. For each line:
  - The first line contains three space-separated integers denoting tp, i and j, where tp = 1, 2 or 3.

## Output format

For each test case in a new line, print Q + 1 space-separated integers denoting the initial value of F(A, B) and F(A, B) after each query. Do not forget to take modulo 998244353.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/array-queries-again-7948f256/
