# Harmonic Triplets

You are given an array A. A triplet is said to be a Harmonic triplet if it satisfies the following conditions :

- i < j < k.
- A[i] <= A[j] >= A[k]

You have to find the harmonicc triplet with the maximum value of A[i]xA[j]xA[k].

You are given q queries, where in each query you are given j-th index and you have to find the harmonic triplet with value at j-th index which has maximum product.

**Note** If there are no elements to the left or right of j which satisfy the given conditions, answer for the given index will be 0.

## Input format

- The first line contains single integer T denoting the number of test cases. T test cases follow.
- The first line of each test case consists of two space-separated integers N,Q denoting size of the array and number of the queries respectively.
- Next line contains N spaced integers denoting contents of the array.
- The next Q lines contain values of j-th index for which you have to find harmonic triplet with maximum product.

## Output format

For each test case, for each query print a single line consisting of the maximum possible product for that query.
