# Ambiguous Tree

For his birthday, Jeffrey received a tree with N vertices, numbered from 1 to N. Disappointed by the fact that there is only one simple path between any two vertices, Jeffrey decided to remedy this by introducing an extra edge in the tree. Note that this may result in a self loop or multiple edge. After introducing an extra edge, Jeffrey wants to know how many pairs of two vertices are ambiguous. Two vertices are ambiguous if there exists more than one simple path between them. Jeffrey has Q queries — he has decided Q possible locations for the extra edge. Please help him find out how many ambiguous pairs there in the tree if he added each of the Q edges to the tree. The tree will revert back to its original state after each query, so queries are mutually independent.

## Input format

- The first line of input will contain N.
- The next N - 1 lines of input will each contain a pair of integers a and b, indicating that there is an edge from vertex a to b.
- The next line of input will contain Q.
- The next Q lines of input will each contain a pair of integers u and v, indicating that Jeffrey is considering putting an extra edge between u and v.

## Output format

Output Q lines, the answers to the queries in the same order as given in the input.
