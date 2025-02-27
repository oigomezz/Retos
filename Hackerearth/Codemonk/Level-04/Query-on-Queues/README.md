# Query on queues

You are given an array containing N integers and you have to answer K queries. Each query contains an integer X which is the index of the i-th (1 based index) element of the queue.

Write a program to determine the following for each query:

- The number of segments containing the index X as the leftmost or the rightmost element. and the number at the index X is >= each element of that segment.

**Segment formation example:** You have 3 numbers 1, 2, and 3.

The possible segments for 3 are [3], [2,3] and [1,2,3]. Similarly, the possible segments for 2 are [2],[1,2].

## Input format

- First line: T (number of test cases).
- First line in each test case: Two space-separated integers N and K.
- Second line in each test case: N space-separated integers (denoting the elements of the queue).
- Next K lines in each test case: X.

## Output format

Print the answer to each query.
