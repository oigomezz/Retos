# [Shuffle Array][link]

Given an array A of N integers. We need to decompose A into K consecutive non empty subarrays such that every integer is present in only one subarray.

Say subarrays are S[1], S[2], S[3], .... , S[K]. Choose an array B , which is a permutation of 1 to K i.e. it is of size K and include every element from 1 to K.

Now, form a new array V = S[B[1]] + S[B[2]] + ...... + S[B[K]].

Aim is to maximize X for array V.

- X = LIS \* LDS - LIS ⊕ LDS, where ⊕ denotes bitwise xor operator.

## Note

- 1 based indexing is followed.
- LIS stands for longest increasing subsequence of V i.e. every element in the subsequence is greater than the previous one.
- LDS stands for longest decreasing subsequence of V i.e. every element in the subsequence is less than the previous one.

## Input format

- First line contains two space-separated integers : N and K.
- Second line contains N space-separated integers denoting the array A.

## Output format

- In the first K lines, print one integer denoting end index of i-th subarray (indexes are 1 based).
- In next line print K space separated integers, denoting array B (permutation of 1 to K)
- End index of subarrays should be in increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/approximate/shuffle-array-3df1e5bb/
