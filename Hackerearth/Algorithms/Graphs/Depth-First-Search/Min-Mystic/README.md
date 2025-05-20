# [Min-Mystic][link]

A magical tree with N vertices and N-1 edges is provided to you. Each of the N-1 edges have some positive weight. Assuming there are X edges in the simple path between vertices A and B, then the separation between the vertices A and B can be determined using the following formula:

- (Total weights of all the edges along the simple path between vertices A and B) × (X % 3)

Now, the mystical value for each vertex is defined as the sum of the separation between this vertex & every other vertex. Your task is to determine the minimum mystical value that a vertex has in the given magical tree.

**Note:** A simple path is a path in a tree that does not have repeating vertices.

## Input format

- The first line contains a single integer T, which denotes the number of test cases.
- For each test case:
  - The first line contains N denoting the number of vertices in the tree.
  - The following N-1 lines contain 3 space-separated integers, u, v, and w indicating that there is an edge between vertices u & v of weight w.

## Output format

For each test case, print the minimum mystical value that a vertex has in the given magical tree in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/min-mystic-3c780194/
