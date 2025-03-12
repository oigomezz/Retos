# [Candy in the box][link]

You have N boxes numbered 1 through N and K candies numbered 1 through K. You put the candies in the boxes in the following order:

- first candy in the first box,
- second candy in the second box,
- ........
- ........
- so up to N-th candy in the Nth box,
- the next candy in (N - 1)-th box,
- the next candy in (N - 2)-th box
- ........
- ........
- and so on up to the first box,
- then the next candy in the second box
- ........ and so on until there is no candy left.

So you put the candies in the boxes in the following order:

1,2,3,...,N,N-1,N-2,...,3,2,1,2,3,...N, N-1,...

Find the index of the box where you put the K-th candy.

## Input format

- The first line contains T denoting the number of test cases. The description of T test cases is as follows:
- Each test case consists of a single line containing two integers N, and K.

## Output format

For each test case, print the index of the box where you put the K-th candy.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/candy-in-the-box-75b63839/
