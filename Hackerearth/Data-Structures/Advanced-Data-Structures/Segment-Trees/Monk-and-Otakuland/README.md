# Monk and Otakuland

Monk lives in Otakuland. Otakuland consists of N vertices and N-1 directed edges. i-th edge is a directed edge either from i-th vertex to i+1-th vertex or from i+1-th vertex to i-th vertex. You are given M Queries. Queries are 2 types:

1. 1 l r - Reverse the direction of the edges between l-th vertex and r-th vertex.
2. 2 f t - Output the minimum number of edges which you have to reverse the direction to arrive from f to t.

## Input format

The first line contains two integers N, the number of vertices and M, the number of queries. The next line will contains N-1 characters which represent the direction of the edges. i-th character is either '>' or '<': '>' represents that only i -> i+1 is valid, '<' represents that only i+1 -> i is valid. The following M lines will each contain a query like the ones mentioned above.

## Output format

For query 2, print the answer in a new line.
