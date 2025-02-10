# Beautiful pair of nodes

You are given a rooted tree having n nodes, rooted at node 1. Every node i has two values associated with itself, A[i] and B[i]. In this tree you have to count total pairs of nodes which are beautiful. A pair of nodes i , j is beautiful if i is ancestor of node j and A[i] < A[j] and B[i] < B[j].

Node i is called an ancestor of some node j, if node i is the parent of node j, or it is the ancestor of parent of node j. The root of a tree has no ancestors.

## Input format

- First line contains a number n as input.
- Next n-1 lines contain two integers u , v denoting that there is an edge between the nodes u and v.
- Next line contains n space separated integers that denote the A[i] value for each node.
- Similarly next line contains n space separated integers that denote the B[i] value for each node.

## Output format

In the output you have to print total good pairs in the tree.
