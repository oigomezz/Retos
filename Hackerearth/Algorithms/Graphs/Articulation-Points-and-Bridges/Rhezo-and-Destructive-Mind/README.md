# [Rhezo and Destructive Mind][link]

Rhezo has bought a graph with N nodes and M edges. He has a destructive mind and often deletes some nodes(and of course its edges to other nodes of the graph).

He will ask you Q queries. Each query is denoted by an integer X, meaning that he will delete the node X. Since he has a destructive mind, he gets satisfied if the the new graph with deleted node has more number of connected components than the original graph.

If satisfied, he wants you to print "Satisfied"(without quotes) and the number of edges that were removed when deleting node X, else print "Not Satisfied"(without quotes). All queries are different, and the original graph is restored after each query.

## Input format

- First line contains N and M as described in the problem statement.
- Each of the next M lines contain 2 integers Ai and Bi, meaning that there is an edge between node A and node B.
- Next line contains a single integer Q, denoting the number of queries.
- Each of the next Q lines contain a single integer X as described in the problem statement.

## Output format

For each of the Q queries, if Rhezo is satisfied(that is the number of connected components of the new graph has increased), print "Satisfied"(without quotes), and the number of edges that will be deleted after a space. Else print "Not Satisfied".

[link]: https://www.hackerearth.com/practice/algorithms/graphs/articulation-points-and-bridges/practice-problems/algorithm/rhezo-and-destructive-mind/
