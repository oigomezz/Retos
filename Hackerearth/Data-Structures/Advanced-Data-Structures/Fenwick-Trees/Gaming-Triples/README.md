# [Gaming Triples][link]

All the Games are not Mathematical at all but Mathematical games are generally favourite of all. Ananya offered such a Mathematical game to Sarika. Ananya starts dictating the rules of the game to Sarika. Sarika finds the game interesting and wishes to play it. Ananya said that they have an array of N elements. Each second either Ananya or Sarika can make a move. First one to make a move can select any 3 elements from the given array which satisfies the following condition.

Let us consider 3 selected elements are A[x1], A[x2], A[x3] so they must follow the given two condition.

1. x1 < x2 < x3
2. y1 < y2 > y3.

where y1 = A[x1] , y2 = A[x2] , y3 = A[x3].

The 3 selected numbers are written down on a piece of paper. One triplet can only be chosen once.

The second player to make a move can also choose any 3 elements A[x1], A[x2], A[x3] such that chosen set of elements fulfill the following two conditions.

1. x1 < x2 < x3
2. y1 > y2 < y3.

where y1 = A[x1] , y2 = A[x2] , y3 = A[x3].

Ananya and Sarika move alternatively and play optimally. Determine the winner of the game and also report the number of seconds for which the game lasts.

## Input format

- First line of input contains a single integer T denoting the number of test cases.
- First line of each test case contains a single integer N denoting the number of elements in the array.
- Next line contains N space separated integers denoting elements of the array.
- Next line of test case contains a single integer 0 if Ananya starts the game and 1 if Sarika starts the game.

## Output format

Output consists of 2\*T lines. 2 lines corresponding to each test case. First line contains name of the winner of the game and second line contains number of seconds for which the game lasts.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/gaming-triples/
