# [Zero path operations][link]

Given a tree with N nodes with some non-negative value assigned to it. Lets say that the value of the i-th node is wi. The beauty of a path between nodes u and v (denoted by B(u,v)) is described as the sum of values of all nodes that lie on the path excluding the nodes u and v. Note that B(u,u) is always zero for any valid node u. Ash is a weird guy. He only likes trees that have ΣΣ B(u,v) = 0. In one operation Ash can change the value of any node to any non-negative value. Ash wants to find the minimum number of operations required so that he starts liking the given tree. But Ash does not have time to solve the problem as he is on his Pokemon adventure. So he needs your help in solving this problem.

## Input format

- The first line contains an integer T denoting the number of test cases.
- The following format is followed for each test case:
  - Next line contains a single integer N denoting the number of nodes in the tree.
  - Next N-1 lines contains two space-separated integers and denoting that there is an edge between u and v.
  - Next line contains N space-separated integers where the i-th integers denotes wi.

## Output format

For each test case, output the minimum number of operations required on a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/zero-path-a7d370fd/
