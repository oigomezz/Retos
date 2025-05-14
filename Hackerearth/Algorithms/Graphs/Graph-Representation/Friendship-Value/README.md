# [Friendship value][link]

You want to place k people in a place shaped like a graph. The graph has n vertices and m edges.

The score of an arrangement is based on the following two factors:

- Friendship is always important even in these tough times of Covid. Here, the i-th person has friendship value fi. A connected component of people with the sum of friendship value equal to s adds s² to score. A connected component is a set of people adjacent to each other. Two persons are adjacent if they are connected with an edge.
- You also need to take care of the health of people. Here, the i-th person has a danger value di. Two adjacent people i and j reduce the score by di x dj.

Your task is to print an arrangement with as high a score as possible. Note that you can drop a person and don't give him a vertice in the graph.

## Input format

- The first line contains k, n, and m.
- The second line contains array f.
- The third line contains array d.
- The last n lines contain the table.

## Output format

Print k integers. The i-th number is the number of the vertex you assigned to the i-th person. Otherwise, print 0 if you do not want to include this person in the arrangement.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/approximate/freindship-and-covid-2-b2d978ae/
