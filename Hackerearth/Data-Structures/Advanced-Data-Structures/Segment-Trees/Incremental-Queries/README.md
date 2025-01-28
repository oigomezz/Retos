# [Incremental queries][link]

You are given an array A consisting of N elements A1, A2,..., An. You must process N queries and there are two types of queries:

- 1 L R: Replace Lth element by R, that is, A[L] = R.
- 2 L R: You are required to print the minimum number of operations to make all elements equal in subarrays A[L], A[L+1],..., A[R].

You can perform the following operation in order to make elements equal:

- Select any index L and replace A[L] with A[L]+1 or A[L]+2.

**Note:** You do not have to modify the original array in a query of type 2.

## Input format

- The first line contains two space-separated integers N and Q.
- The second line contains space-separated integers A1, A2, ..., An.
- Each of next Q lines contains three integers type L,R denoting the type of query and its parameters.

## Output format

Print a single integer for every query of the second type.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/incremental-queries-a7a71194/
