# [Break the adjacency][link]

Alex on his walk to Forest of leaf discovers N sticks lying in front of him. Each stick has two values represented by two arrays arr and price of size N where in array arr, arr[i] (0 <= i <= N-1) denotes length of i-th stick and array price, price[i] (0 <= i <= N-1) denotes price to increment length of i-th stick by 1 unit.

Alex calls an array Broken Adjacency when none of the adjacent sticks has equal length. A stick i is adjacent to stick i-1 (if any) and stick i+1 (if any). He wants to find the minimum cost to achieve Broken Adjacency. To do so, in 1 move he can increment the length of any i-th stick by 1 unit at the price of price[i].

Can you help him find the minimum cost to achieve his goal?

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first input line of each test case contains one integer N, denoting the number of sticks found.
- The second line contains N space-separated integers denoting the elements of array arr.
- The third line contains N space-separated integers denoting the elements of array price.

## Output format

Print the minimum cost to make given sticks to Broken Adjacent sticks.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/break-the-adjacency-290d35ba/
