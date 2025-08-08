# [When the Integers got upset!][link]

Puchi was crossing a river by jumping over stepping stones, carrying a bag containing N integers. Our Monk saw him from the banks and shouted out to him. Shaken by the sudden shout, Puchi dropped the bag in the river and all the integers got wet! This upset the integers.

There are N stepping stones available ahead. Puchi wants to dry these integers on these stones, such that each stone contains a single integer. The upset value of the i'th integer Ai (after rearrangement of the integers) is (Ai ^ Ai-1 ^ Ai-2) times Pi for i ≥ 2, and 0 otherwise. (where '^' is the bit wise XOR operator). Here, i represents the position of the said integer.

Puchi asks our Monk to find an order of arranging the numbers on the stones, such that sum of upset values is minimized. Help our Monk find the order, given the arrays A and P.

## Input format

- First line contains T. T test cases follow.
- First line of each test case contains an integer N.
- Second line of each test case contains N integers, forming the array A.
- Third line of each test case contains N integers, forming the array P.

## Output format

Print the answer to each test case in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/bit-masking/practice-problems/algorithm/when-the-integers-got-upset/
