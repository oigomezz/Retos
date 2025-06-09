# [Two Trees][link]

There exits an edge-weighted directed tree rooted at node , where edges are directed from child towards the parent, and each edge has a positive weight. Let's call this tree Tree1.

There exists another tree, Tree2 which is constructed from Tree1 as: Copy entire Tree1 and double each of it's edge value (Edges remain directed in Tree2 as well).

There also exits an undirected weighted edge, with weight w(v) between node v of Tree1 and node v of Tree2, for all 1 <= v <= n (where n is the number of nodes in the trees).

You will be given q queries of the form u,v where v will be ancestor of u. You will have to find the length of the shortest path from u to v in Tree2 (mean you've to start in node u in Tree2 and reach node v in Tree2).

## Input format

- The tree is given in input as undirected tree, rooted at 1.
- First line contains a single integer n - no. of nodes in the tree.
- Each of the next n-1 lines contains 3 space separated intergers - u,v,x. Indicating there is an edge between u and v with weight x in Tree1.
- Next line contains n space-separated integers - w(v) for each node from 1 to n.
- Next line contains a single integer - q - no. of queries.
- Each of the next q lines contains 2 space seperated integers - u,v. It is guranteed that v will be an ancestor of u.

## Output format

For each query print a single integer in a separate line which is the answer to the query.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/two-trees-ee18cad2/
