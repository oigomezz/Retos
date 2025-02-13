# [3B - Bear and Special Dfs][link]

Bear recently studied the depth first traversal of a Tree in his Data Structure class. He learnt the following algorithm for doing a dfs on a tree.

```c++
void dfs(int v,int p){
    vis[v] = 1;
    for(int i=0;i<G[v].size();++i){
        if(G[v][i]!=p)
            dfs(G[v][i],v);
    }
}
```

Now he was given an array A, Tree G as an adjacency list and Q queries to answer on the following modified algorithm as an homework.

```c++
void dfs(int v,int p){
    vis[v] += 1;
    for(int j=1;j<=A[v];++j){
        for(int i=0;i<G[v].size();++i){
            if(G[v][i]!=p)
                dfs(G[v][i],v);
        }
    }
}
```

The Q queries can be of the following two types :

- 1 v x : Update A[v] = x. Note that updates are permanent.
- 2 v: Initialize vis[u] = 0 ∀ u ∈ [1, N]. Run the above algorithm with call dfs(1,-1).

## Input format

- The first line contains two integers N and Q, the number of vertices in the tree and the number of queries respectively.
- Next N - 1 lines contains the undirected edges of the tree.
- The next lines contains N integers denoting the elements of array A.
- Following Q lines describe the queries.

## Output format

For each query of type 2, print the required result mod 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/utkarsh-and-special-dfs/
