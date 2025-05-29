# [Skrtel !][link]

**Stevie:** "The more you play with Christmas Trees, the more addicted you are to them. Let's go on". Legends serve a club selflessly for ages without any noise off the pitch. Do you remember the headed goal vs the Gunners with a highly bandaged head by this guy : ?

You are given a Tree T consisting of N nodes where node i of the tree has number Ai written on it. Now, you need to process 2 kinds of queries on this tree.

- 1 X Y: Update the number written on node with index X to Y.
- 2 U V K: Find if the product of number written on each nodes lying on the path from node U to V is divisible by the number K.

The answer to the second kind of query is either a YES or NO .

Can you answer all the given queries efficiently?

## Input format

- The first line contains 2 space separated integer N and Q denoting the number of nodes in tree T and the number of queries respectively.
- The next line contains N space separated integers, where the i-th integer denotes the number initially written on node i i.e. Ai.
- Each of the next N-1 lines contains 2 space separated integers U and V denoting an undirected edge between nodes with index U and V in tree T. It is guaranteed that the input edges are such that it always forms a valid tree.
- Each of the next Q lines contains a query of either of the two types on a single line.
  - 1 X Y.
  - 2 U V K.

## Output format

Print the answer to each query of type 2 in the order they appear in the input on a new line. The answer to the queries shall be either a YES or a NO.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/skrtel/
