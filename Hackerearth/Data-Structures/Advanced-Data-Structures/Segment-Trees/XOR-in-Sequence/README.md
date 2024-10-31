# XOR in Sequence

Given a sequence A consisting of N integer elements: A1, A2, .., AN.

Your task is to answer Q queries. Each query requires to count the number of pairs of integers (i, j) such that 1 ≤ i ≤ j ≤ N, and L ≤ Ai XOR Ai + 1 XOR Ai + 2 XOR ... XOR Aj ≤ R where L and R are given.

## Input format

- The first line is T - the number of test cases. Then T test cases follow.
- Each test case consists of Q + 3 lines.
  - The first line is N.
  - The second line contains N integer denoting the sequence A.
  - Then the next line is Q - the number of quries you must answer.
  - The next Q lines, each line consists of two integer L and R.

## Output format

For each query, print the answer.
