# [Operations and tree][link]

Yuqi has an rooted indexed tree T of N nodes indexed from 1 to N. The node 1 is the root. Now on each node there is a value V[i].

He can cast several kinds of magic:

- Magic Kind 1: given a,b increase the value in the subtree of node a by b.
- Magic Kind 2: given a,b increase the value of node a by b.
- Magic Kind 3: given a if a is in the Blacklist remove it, otherwise add it into the blacklist.
- Magic Kind 4: given a.tell Yuqi the value of node a.

Nodes in Blacklist's value will not be affected by any other magic until it's removed.

Now he gives you the list of magic to proceed. You need to proceed them in order. Note that value of any node can be negative at any moment.

## Input format

- The first line contains one integer N
- The next N-1 lines each contains two numbers x,y indicating an edge.
- The next line contains N integers, the array V.
- The following line contains one integer q - the number of magic to proceed.
- Then next q lines can be:
  - 1 a b Magic Kind 1
  - 2 a b Magic Kind 2
  - 3 a Magic Kind 3
  - 4 a Magic Kind 4

## Output format

For each magic 4, output the answer.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/tree-party-score-ba8a07b7/
