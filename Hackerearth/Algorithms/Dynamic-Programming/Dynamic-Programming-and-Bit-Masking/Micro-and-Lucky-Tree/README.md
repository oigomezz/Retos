# [Micro and Lucky Tree][link]

Micro purchased a tree having N nodes numbered from 1 to N. It is rooted at node numbered 1. But unfortunately that tree turned out to be bad luck. After he purchased that tree, he lost his job and girlfriend. So he went to his astrologer friend Mike for help.

Mike told him to assign a value in the range 1 to M (inclusive) to each node making sure that luck factor of all leaf nodes is 1. Luck factor of a leaf node v is defined as GCD of values of all nodes lying in path from root to v (inclusive). Now Micro wants to know how many ways are there to make his tree lucky. That's where Mike failed, so he asked for your help.

## Input format

- First line consists of a single integer denoting N and M.
- Each of the following N-1 lines consists of two space separated integers X and Y denoting there is an edge between nodes numbered X and Y.

## Output format

Print the number of ways to make the tree lucky. Since the answer can be large, print it modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/micro-and-lucky-tree/
