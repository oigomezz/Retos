# [Cluster Features][link]

Given n 2-dimensional data objects or points in a cluster, we can define the centroid (x0,y0), radius R and diameter D of the cluster where R is the average distance from member objects to the centroid, and D is the average pairwise distance within the cluster. Both R and D reflect the tightness of the cluster around the centroid.

**Note:** Take R = 0 for n < 1 and D = 0 for n < 2.

Given p data objects or points, you are supposed to answer q queries. In the i-th query, you consider only the points whose x-coordinate lies in [x1i, x2i] and y-coordinate lies in [y1i, y2i] as a single cluster. For each query you have to find the centroid, radius and diameter of the cluster. Since the values can be non-integer, you have to print the value of nX0 + ny0 + n²R² + n(n-1) D².

## Input format

- The first line contains two integers p and q denoting the number of data objects or points and the number of queries/clusters respectively.
- Next p lines contains two-space separated integers denoting xi and yi. The coordinates of i-th data point.
- Next q line contains four space-separated integer denoting x1i, x2i, y1i and y2i respectively.

## Output format

Output q lines each containing a single integer. i-th line denotes the value of nX0 + ny0 + n²R² + n(n-1) D² of the i-th cluster.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/cluster-features-b6d64df9/
