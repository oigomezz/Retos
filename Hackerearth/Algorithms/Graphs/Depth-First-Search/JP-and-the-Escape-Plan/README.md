# [JP and the Escape Plan][link]

JP is stuck in a grid of buildings of size N \* M, after he is dropped from a helicopter. He will be able to escape this grid if he can reach to any building that is on the boundary of grid. He can jump from one building to the other if and only if :

1. The buildings shares the edges with each other, i.e are adjacent (not diagonally adjacent)
2. The building to which he is jumping should be of the same height of the building on which he is standing OR the building to which he is jumping should have height at max J less than the one on which he is standing.

The top left building will have the co-ordinates (1,1) and the bottom right will have the co-ordinates (N,M)

## Input format

- The first line contains two space separated integers N and M Each of the next N lines contains M space separated integers denoting the heights of the buildings.
- Next line contains three space separated integers Dx, Dy and J, Dx,Dy are the co-ordinates of the building where JP is dropped.

## Output format

On the first line, print "YES"(without quotes) if he can reach any building on the boundary of the grid else print "NO"(without quotes).

If the answer is YES, on the next line print a single integer K, the length of the path JP must travel along to reach his destination. In each of the next K lines, print 2 space separated integers (x,y). It is necessary that the first co-ordinate along the path must be (Dx, Dy), and the last co-ordinate along the path must be present on the boundary of the grid.

A path is considered to the valid if and only if it does not contain any repeated co-ordinates, and does not violate any rules of JP's travel conditions mentioned above. In the case of printing a wrong path, you shall get a Wrong Answer. It is not necessary that the printed path should be the shortest one available.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/approximate/jp-and-the-escape-planapprox/
