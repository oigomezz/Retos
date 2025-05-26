# [One and only flow][link]

You are given a network of directed graph of N vertices and M edges, where every edges' capacity is 1. An ordered pair (u,v), u != v is good, if the maxflow is exactly 1 upon setting u as the source vertex and v as the sink vertex of the flow network. Find out if all of the ordered pairs (u,v), u != v are good or not.

## Input format

- First line: An integer T, number of testcases.
- Each test case's:
  - First line: Two integers N,M.
  - i-th of the next M lines: two integers u,v, a directed edge from u to v.

## Output format

Print T lines, i-th line contains answer for i-th testcase. For a testcase, the answer is "Yes" if every ordered pair is good, "No" otherwise.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/one-and-only-flow-740e0808/
