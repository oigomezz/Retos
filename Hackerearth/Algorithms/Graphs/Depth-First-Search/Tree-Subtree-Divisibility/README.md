# [Tree Subtree Divisibility][link]

Alice has received a beautiful tree as a gift from her math teacher. This tree has N nodes connected by N-1 edges, and each node is assigned a value represented by Ai.

Alice enjoys playing with this tree by cutting certain edges and dividing it into multiple subtrees. She has a favorite number X, and she's curious to find out the number of ways she can cut the tree into subtrees so that the sum of values in each subtree is divisible by X. The cutting order of the edges doesn't matter.

Help Alice solve this interesting problem by determining the count of good cuttings she can make when dividing the initial tree into 1 subtree, 2 subtrees, 3 subtrees, and so on, up to N subtrees.

- A good cutting is a cutting in which sum of all values of each subtree is divisible by X .

As the number of good cuttings can be huge you need to print the answer modulo 10⁹ + 7.

## Input format

- First line of the input contains an integer T, representing the number of test cases.
- The first line of each test case contains 2 integers N, X.
- The next line of each test case contains N integers separated by a space, representing the array A.
- The next N-1 lines of each test case contains integers each, representing an edge of the tree.

## Output format

For each test case, output N integers separated by a space telling the count of good cuttings when dividing the tree into 1 subtree, 2 subtrees, 3 subtrees, and so on, up to N subtrees.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-subtree-divisibility-db02e0dc/
