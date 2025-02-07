# [Xsquare And Array Operations][link]

Xsquare loves to play with arrays a lot. Today, he has an array A consisting of N distinct integers. He wants to perform following operation over his array A.

- Select a pair of consecutive integers say (Ai,Ai+1) for some 1 ≤ i < N. Replace the selected pair of integers with the max(Ai,Ai+1).
- Replace N with the new size of the array A.
- Above operation incurs a cost of rupees max(Ai,Ai+1) to Xsquare.

As we can see after N-1 such operations, there is only 1 element left. Xsquare wants to know the most optimal transformation strategy to reduce the given array A to only 1 element.

A transformation strategy is considered to be most optimal if it incurs minimum cost over all possible transformation strategies.

## Input format

- First line of input contains a single integer T denoting the number of test cases.
- First line of each test case starts with an integer N denoting the size of the array A.
- Next line of input contains N space separated integers, where i-th element denotes the value Ai.

## Output format

For each test case, print the minimum cost required for the transformation.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/xsquare-and-array-operations/
