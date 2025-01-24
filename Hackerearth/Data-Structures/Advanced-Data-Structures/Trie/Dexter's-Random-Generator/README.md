# [Dexter's Random Generator][link]

Dexter has recently constructed a random generator. This generator works on a tree of N nodes. The information about the tree has to be fed into the generator in order for it to start working.

Each node, u of the tree has a value A[u] associated with it. The generator works as follows:

It takes as input two integers, u and v. It then outputs two integers X and Y. X can be either A[u]or A[v], with equal probability. Now, the generator selects a node i randomly and with equal probability from the path u-v (including u and v) in the tree and outputs the value of Y as A[i].

Let the above process be denoted by: Process(u,v), which takes input a pair of integers and outputs a pair of integers (X,Y).

Now, Hannah has been invited to test the random generator constructed by Dexter. Hannah has Q questions. Each question is as follows:

Hannah selects two nodes u and v of the tree. She wants to know the maximum value of Query(u,v).

Query(u,v) is defined below:

    Query(u,v):
        (X1,Y1) = Process(u,v)
        (X2,Y2) = Process(u,v)
        A = X1 ^ Y1
        B = X2 ^ Y2
        return abs(A-B)

^ denotes the bitwise exclusive or operator.

Also note that Process(u,v) runs for (X1,Y1) and (X2,Y2) independent of each other.

Dexter needs your help in answering the questions of Hannah.

## Input format

- First line of the input contains two integers N and Q, the number of nodes in the tree and the number of questions that Hannah asks from Dexter, respectively.
- Next line contains N space separated positive integers, where ith integer denotes the value at ith node, i.e., A[i].
- Next N-1 lines describe the structure of the tree. Each of these lines contain two space separated integers p and q. There is an undirected edge between p and q.
- Next Q lines, each line denoting a question from Hannah, which contains two space separated integers u and v, which means that Hannah has chosen these two nodes for that query.

## Output format

You are supposed to output Q lines. The ith line contains the answer for the ith query.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/dexters-random-generator/
