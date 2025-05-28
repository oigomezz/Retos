# [Words And Trees][link]

You are given a rooted tree with N nodes. Each node contains a lowercase English letter. Node with label 1 is the root.There are Q questions of the form

- X S: Here X is the root of subtree and S is a string.

For each question, let T be the string built using all the characters in the nodes of subtree with root X (each subtree node character comes exactly once) .
For each question, print minimum number of characters to be added to T , so that the we can build S using some characters of string T (each character of string T can be used at most once).

**Hint:** Find all the characters coming in each subtree and use it to get the answer to each question.

## Input format

- The first line of input consists of two space separated integers N and Q that are number of nodes in the tree and number of questions respectively.
- Next line will contain N space separated lowercase English letters, where i-th letter will be the letter stored in node with label i.
- Each of the next N-1 lines contains two space separated integers u and v that denote there is an edge between nodes with labels u and v.
- Next Q lines follow. Each line will contain an integer X that denotes the node label and a string S separated by a single space.

## Output format

For each query, print the required answer in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/words-and-trees-f9ef202c/
