# [Memory Reader][link]

There is a new AI in town. It reads through horizontal strips of memory. Let the strip of memory be divided into blocks numbered 1,2,3,... etc. There is good data at some integer points on the memory given in an array memory. The AI can only read at these points. The AI aims to read the last point of good memory. Also, the AI can only move in the forward direction.

To read a memory, it can move from one good point to another. It can move its reader pointer to either L-1 or L or L+1 points if the length of its last jump was L. Initially, it is at point 0 (which is always a good memory). The first move can only be to the first good memory point. Determine if it can move to the last memory. It is ensured that the good memory points are given in sorted order.

**Note:** The AI doesn’t need to read all the good memory points.

## Input format

- The first line contains T, denoting the number of test cases.
- The first line of each test case contains one integer N, denoting the number of good memory points.
- The second line of each test case contains an array memory of N space-separated integers, denoting the position of the good memory points.

## Output format

For each test case, print the string YES if the AI can read the last memory point, else print the string NO.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/memory-reader-758b9c5b/
