# [Reach Quickly][link]

You are given a connected graph consisting of N vertices and M bidirectional edges. You are also given an array A of length X and an array B of length Y.

The time to reach a vertex V from an array of vertices S is defined as the minimum of the shortest distance between U and V for all U in S.

The cost of an array of vertices S is defined as the sum of the time to reach vertex V from S for all V in B.

Find the last index of the smallest prefix of A having the minimum cost.

## Input format

- The first line of input contains a single integer T, denoting the number of test cases.
- The first line of each test case contains two integers N and M, denoting the number of vertices and the number of initial edges respectively.
- The following M lines contain 2 integers u and v, denoting a bidirectional edge between vertex u and vertex v.
- The next line contains X and Y, denoting the length of the arrays A and B respectively.
- The next line contains X integers, denoting the elements of array A.
- The last line contains Y integers, denoting the elements of array B.

## Output format

For each test case, print the last index of the smallest prefix of A having the minimum cost.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/reach-quickly-a0f17062/
