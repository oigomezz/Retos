# [Velma and Queries][link]

The "Mystery Incorporated" once went for an investigation. Since Scooby and Shaggy always create havoc during investigation, Velma decided to give them a question so as to keep them busy.

Velma gave them a tree consisting of N nodes, rooted at node 1 with a number in each node, and asked them several queries. Each query was of the form u l and they had to find the sum of values of all nodes situated at a depth l and were in the subtree of u.

Since Scooby and Shaggy are dumb, they need your help in solving this problem.

## Input format

- The first line will contain the number of test cases T.
- The first line of each test case will contain two integers N and Q (1 ≤ N, Q ≤ 100,000) - the number of nodes and the number of queries.
- The second line of each test case will contain N integers a1, a2, ..., aN, where ai (1 ≤ ai ≤ 10,00,000) is the value stored at the ith node.
- The next N-1 lines of each test case will contain two integers u and v, meaning that there is an edge connecting u and v.
- The next Q lines contains the queries each of the form u and l.

## Output format

For each query in every test case, print the answer to the query on a single line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/velma-and-queries/
