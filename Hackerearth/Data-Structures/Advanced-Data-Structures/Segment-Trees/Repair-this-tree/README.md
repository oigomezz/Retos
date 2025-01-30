# [Repair this tree][link]

You are given a rooted tree T of n nodes and a graph G of n nodes. Initially, the graph G has no edges. There are two types of queries:

- 1 x y w: Add an edge of weight w between nodes x and y in G.
- 2 v p: Consider that the edge between v and its parent in T is deleted which decomposes into 2 connected components. You need to find the sum of weights of all edges like x in G such that:
  - The weight of x is divisible by p.
  - If an edge is added in T between the same endpoints as x then again we will get a tree (it will connect the two components). Note that the edge is deleted only for that particular query.

## Input format

- First line: Two integers n,q
- Second line: n-1 integers where i-th integer is the number of the parent of (i+1)-th node. 1 is the root of the tree.
- Next q lines: Contains a description of queries. One query per line as described in the question, p is prime.
- The graph G may have self-loops and multiple edges.
- Queries are encrypted, hence you have to answer queries online. If lastAns is the answer of the last query of type 2 (zero if not present), then you must decrypt queries as follows:
  - 1 x y must be decrypted as x = (x + lastAns - 1) mod n+1, y = (y + lastAns -1) mod n + 1.
  - 2 v must be decrypted as v = (v + lastAns - 1) mod (n-1)+2.

## Output format

For each query of the second type, print the answer in a seperate line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/repair-tree-339749d4/
