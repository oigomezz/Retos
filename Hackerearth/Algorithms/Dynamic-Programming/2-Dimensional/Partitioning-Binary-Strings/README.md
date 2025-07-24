# [Partitioning binary strings][link]

You are given a binary string of 0's and 1's.

Your task is to calculate the number of ways so that a string can be partitioned by satisfying the following constraints:

1. The length of each partition must be in non-decreasing format. Therefore, the length of the previous partition must be less than or equal to the length of the current partition.
2. The number of set bits in each partition must be in non-decreasing format. Therefore, the number of 1's that are available in the previous partition must be less than or equal to the number of 1's that are available in the current partition.
3. There should be no leading zeroes available in each partition.

**Note:** The string as a whole is a valid partition.

Print the number of ways modulo 10⁹ + 7.

## Input format

- The first and only line contains n and s that represents the length of the string and binary string.

## Output format

Print the number of ways to partition the binary string.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/partitioning-binary-strings-857646e9/
