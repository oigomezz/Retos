# [Easy Queries][link]

You are given an array of size N in which the value of the elements are either 0 or 1. All the elements of array are numbered from position 0 to N-1.You are given some queries which can be of following 2 types.

- 0 index: In this type of query you have to find the nearest left and nearest right element from position index in the array whose value is 1.
- 1 index: In this type of query you need to change the value at positon index to 1 if its previous value is 0 or else leave it unchanged.

**Important Note:** If there is no position with value 1 on the left side of any index in query then print -1 instead of left index and similarly if there is no value 1 in right side of the value index in that query then print -1 in place of the answer for right element.

## Input format

- First line contains 2 integers N and Q denoting the number of elements in array and number of queries.
- Next line contains N elements denoting the array.
- Next Q lines contains integer each denoting the any type of Query.

## Output format

For each query print left and right nearest element seprated by space.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/easy-queries-751f9372/
