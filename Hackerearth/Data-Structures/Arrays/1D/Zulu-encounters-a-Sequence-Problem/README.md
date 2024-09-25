# Zulu encounters a Sequence Problem

Zulu is good in maths. He loves to play with numbers. One day while browsing through a book, he encountered a nice problem. In the problem, he was given an array A of N numbers.

For each index i in the array we define two quantities. Let r be the maximum index such that r >= i and sub-array from i to r (inclusive) is either non-decreasing or non-increasing. Similarly, let l be the minimum index such that l <= i and sub-array from l to i (inclusive) is either non-decreasing or non-increasing. Now, we define points of an index i to be equal to max(|Ai - Al|, |Ai - Ar|). Note that l and r can be different for each index i.

The task of the problem is to find the index of the array A which have the maximum points.

Since the problem seems a bit harder, Zulu is struck. Can you solve this problem for Zulu?

## Input format

In the first line of input, T will be given which is the number of test cases. For each of the test case, a single integer N will be given in the first line. In the second line, N space separated integers will be provided.

## Output format

For each of the test cases, output the points of the index which have maximum points in the array in a separate line.
