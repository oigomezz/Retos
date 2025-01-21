# [Suarez][link]

**Stevie:** " The second half of a programming contest is just as important as the second half of a football match, it's the decisive part ". So, here you are presumably having got over the first half.

You are given N segments [L,R], where L <= R. Now, you need to answer some queries based on these segments.

Overall, you need to answer Q queries. In each query you shall be given 2 integers K and X. You need to find the size of the Kth smallest segment that contains point X.

If no K segments contain point X , print 1 instead as the answer to that query.

A segment [L,R] is said to contain a point X, if L <= X <= R. When we speak about the Kth smallest segment, we refer to the one having the Kth smallest size. We define the size of a segment to be the number of integral points it contains, i.e. R + 1 - L.

## Input format

- The first line contains a single integer N,
- Each of the next N lines contains 2 space separated integers, where the 2 integers on the ith line denote the start and end points of the ith segment given to you.
- The next line contains a single integer Q.
- Each of the next Q lines contains 2 space separated integers K and X.

## Output format

Print the ansnwer to each query on a new line.

[link]: https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/suarez/
