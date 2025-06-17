# [Fredo's Crush][link]

Fredo has crush on a girl in his class. He went to ask her out for a date. She, being a coder, gave her a simple graph with N vertices and M edges and asked him to solve a problem on the graph in order to go on a date with her. The problem says:

Let there be some functions defined below:

For each vertex in the graph:

S = max (sum of all vertices lying in the maximum length simple path ending at that vertex)

That is, if there are two simple paths with length 3 ending at some vertex and there can be no simple path with length greater than 3, and P be the sum of vertices of first path and Q of second. So, S = max(P,Q).

Let:

- A = minimum value of S[i] (1 <= i <= N)
- B = maximum value of S[i] (1 <= i <= N)

You are given an equation Ax = By. Find the minimum value of x and y satisfying the equation.

**Note:** If there are no simple paths ending at some vertex, S for that vertex will be number of that vertex. A simple path is a path in a graph which does not have repeating vertices.

## Input format

- First line contains an integer T denoting the number of test cases.
- First line of each test case consists of two space separated integers denoting N and M.
- The following M lines consist of two space separated integers X and Y denoting there is an edge between vertices X and Y.

## Output format

For each test case, print the values of x and y (space separated) in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/hamiltonian-path/practice-problems/algorithm/fredos-crush-2/
