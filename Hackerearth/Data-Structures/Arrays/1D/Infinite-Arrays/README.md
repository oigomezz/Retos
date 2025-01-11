# [Infinite arrays][link]

You are given an array A of size N. You have also defined an array as the concatenation of array for infinite number of times.

For example, if A = {A1,A2,A3}, then B = {A1,A2,A3,A1,A2,A3,A1,A2,A3,...}.

Now, you are given Q queries. Each query consists of two integers, Li and Ri. Your task is to calculate the sum of the subarray of N from index Li to Ri.

**Note:** As the value of this output is very large, print the answer as modulus 10⁹ + 7.

## Input format

- First line: T denoting the number of test cases.
- For each test case:
  - First line: Contains N, the size of the array.
  - Second line: Contains N space-separated integers corresponding to Ai.
  - Third line: Contains Q denoting the number of queries.
  - Fourth line: Contains Q space-separated integers corresponding to Li.
  - Fifth line: Contains Q space-separated integers corresponding to Ri.

## Output format

For each test case, print Q space-separated integers that denote the answers of the provided Q queries. Print the answer to each test case in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/infinity-array-715a233b/
