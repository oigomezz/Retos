# [Final battle][link]

Monique and Paul both enjoy math and programming a lot. A few days ago they decided to compete against each other in many kinds of problem solving competitions. They solved hundreds of problems, but they still have not decided who the winner is, because the current score is surprisingly a draw. Monique gets impatient, and proposed a final game to decide the battle between them. The game is played as follows:

First, Monique constructs a tree with N nodes and binary weights on the edges of the tree. The weights are not known initially, but the structure of the tree is. After that, she writes down a list of Q distinct queries of the form:

query(v,u) : returns a parity of the sum of values on edges on the path from node v to node u in the tree. Each query has assigned a cost C[u][v] denoting the cost of asking that query.

Finally, she gives Paul two days to find the number of subsets S of the set of all queries such that after asking all queries from S, Paul can be sure what values are assigned to all edges of the tree Monique constructed and that the sum of costs of queries in S is the lowest from all such subsets. Since this number can be very large, Paul has to return it modulo 10⁹ + 7.

The task is to help Paul solve the problem, so he can defeat Monique.

## Input format

- First line there are two space separated integers N and Q denoting the number of nodes in the tree and the number of all possible queries.
- In each of the next N-1 lines there are two space separated integers v,u denoting that there is an edge between nodes v and u in the tree.
- In each of the following Q lines there are three space separated integers v,u,C[u][v] denoting a single queries query(v,u), where C[u][v] is the cost of asking the query.

## Output format

In a single line output a single integer denoting the answer to the problem.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/final-battle/
