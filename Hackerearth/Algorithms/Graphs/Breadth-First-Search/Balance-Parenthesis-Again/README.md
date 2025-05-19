# [Balance Parenthesis Again][link]

Given a set of N nodes, where each node has a character A[i] associated with it. A[i] can be either an opening bracket ( or a closing bracket ). Construct a tree using N nodes numbered 1 to N such that the value of the given function Z is maximized.

Z = ΣΣ F(i,j), where F(i,j) = Length of the longest balanced parenthesis substring on the simple path between node i and node j.

A string is said to be balanced if

- Empty string is a balanced string.
- if s is a balanced string, then (s) is also a balanced string.
- if s and t are balanced strings, then stt (concatenation of s and t) is also a balanced string.

## Input format

- The first line contains an integer N denoting the number of nodes in the tree.
- The next line contains a string A of length N where each character denotes the value of each node.

## Output format

- Print N - 1 lines where each line contains
  - Two space-separated integers a, b denote an edge between nodes a and b in the tree.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/approximate/balance-parenthesis-again-b52594ac/
