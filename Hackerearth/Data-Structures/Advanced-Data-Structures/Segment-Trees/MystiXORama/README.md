# [MystiXORama][link]

In a quaint village, there lived a mathematician named Alice. One day, the villagers approached her with a unique challenge. They had an array A of size N, that held the secrets of their village, and they needed answers to their questions. These questions came in the form of Q queries.

Each query was a request for enlightenment, presented with four mysterious numbers L, R, X, and Y. For each query, Alice embarked on a journey through the array, focusing on the range from L to R. She carefully counted how many times each number appeared in this range (from L to R).

With this newfound knowledge, she weaved a tapestry of wisdom in the form of a new array, B. For every i from 1 to N:

- B[i] = Bitwise XOR of all the numbers that occur exactly i times in the range L to R of array A.

If none of the elements in the range L from R to occurred times, she simply set B[i] = 0.

Finally, Alice presented the villagers with the answer to their query, which was nothing short of a revelation. The answer for each query was the sum of the elements in her array B, but only from position X to Y, for the villagers believed that these specific positions held the key to their query's solution.

You now have to help Alice in completing this challenge.

## Input format

- The first line contains a single integer T, which denotes the number of test cases.
- For each test case:
  - The first line contains N denoting the size of array A.
  - The second line contains N space-separated integers, denoting the elements of A.
  - The next line contains Q denoting the number of queries.
  - The next Q lines contain 4 space-separated integers, denoting L, R, X and Y.

## Output format

For each test case, print the answer for each query in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/mystixorama-26468c50/
