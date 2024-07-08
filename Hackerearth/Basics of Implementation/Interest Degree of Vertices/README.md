# Interest Degree of Vertices

You are given a rooted tree with n vertices. There is a number written on each leaf (a vertex contains degree 1 and the root node can be a leaf if it has just one child). The interest degree of each vertex is the sum of numbers written on leaves in subtree on this vertex. In each step, you can change the number written on a leaf by 1. How many steps are required to make the interest degree of all of the nodes equal?

**Note:** You can change the number written on a leaf to negative values.

## Input format

1. First line: n
2. Next line: n-1 numbers where the ith number is pi denoting the parent of (i+1)th node. **Note:** Node 1 is the root
3. Third line: n numbers where the ith of them is ai denoting the number that is written on vertex i. **Note:** It is guaranteed that if i is not a leaf, then ai = 0.

## Output format

Print the minimum number of steps that are required to make the interest degree of all of the nodes equal.
