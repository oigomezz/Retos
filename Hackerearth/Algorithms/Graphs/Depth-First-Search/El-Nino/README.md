# [El Nino !][link]

**Stevie:** "The best part about Christmas is a Christmas tree. Fantastic to play with". A great goalscorer is one who is remembered even years after he left, just like this guy

You have been given a tree T consisting of N nodes rooted at node 1 and an array A consisting of M distinct integers.

Now, you need to find the number of distinct triplets (U,V,K) in tree T such that node V lies in the subtree rooted at node U, and the distance between them is exactly Ak. We call the distance between 2 nodes to be the number of edges lying in the shortest path among them.

2 triplets (Ui,Vi,Ki) and (Uj,Vj,Kj) are considered to be distinct, if Ui != Uj or Vi != Vj or Ki != Kj.

Can you do it ?

## Input format

- The first line contains 2 space separated integers N and M.
- The next line contains M pairwise distinct space separated integers, where the i-th integer denotes Ai.
- The next line contains N-1 space separated integers, where the i-th integer denotes the parent of node i+1 in tree T.

## Output format

Print a single integer denoting the required number of valid triplets in tree T

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/el-nino/
