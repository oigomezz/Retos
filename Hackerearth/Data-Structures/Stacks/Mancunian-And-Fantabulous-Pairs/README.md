# [Mancunian And Fantabulous Pairs][link]

First off, some definitions.

An array of length at least 2 having distinct integers is said to be fantabulous iff the second highest element lies strictly to the left of the highest value. For example, [1, 2, 13, 10, 15] is fantabulous as the second-highest value 13 lies to the left of highest value 15.

For every fantabulous array, we define a fantabulous pair (a, b) where a denotes the index of the second-highest value (1-indexed) and b denotes the index of the highest value (1-indexed). In the above array, the fantabulous pair is (3, 5).

Mancunian challenges you to solve the following problem. Given an array, find the total number of distinct fantabulous pairs over all its subarrays.

## Input format

The first line contains an integer N denoting the length of the array. The next line contains N distinct integers denoting the elements of the array.

## Output format

Output a single integer which is the answer to the problem.

[link]: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/mancunian-and-fantabulous-pairs/
