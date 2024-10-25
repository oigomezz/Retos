# The maximum distance

You are given an array a1,a2,...,an consisting of N elements. You are given Q queries. Each query is of the following types:

1. The format of the first type of query is 1 L R x. You must increase the values of all elements in range L to R (both inclusive) by integer x.
2. The format of the second type of query is 2 L R y. You must multiply the values of all elements in range L to R (both inclusive) by the integer y.
3. The format of the third type of query is 3 z. You are required to find the maximum distance between elements that are equal to z in the array. If the element is not present in the array, print -1.

## Input format

- The first line contains an integer N.
- The next line contains N integers a1,a2,...,an denoting the elements of the array.
- The next line contains Q denoting the number of queries.
- The next Q lines contain one of the 3 queries mentioned above.

## Output format

For every query of Type 3, print an integer denoting the maximum distance j - i + 1 where 1 <= i,j <= n.
