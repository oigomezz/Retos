# [Another Problem][link]

While working on his project, Rishi ended up with an interesting problem as follows:

There is a string S which is broken down into N chunks (substrings) satisfying the below constraints:

1. For each chunk except the first, starting 4 characters will be overlapping with ending 4 characters of atleast one chunk.
2. For each chunk except the last, ending 4 characters will be overlapping with starting 4 characters of atleast one chunk.

Your task is to find original message from the given chunks. If multiple solutions exists, then print all of them in lexicographical order.

**Note:** Number of chunks and overlaps in each test case are generated in a way that it will always pass within given time constriants.

## Input format

- First line contains an integer N- the number of chunks.
- The next N line's contain a string each - representing a chunk

## Output format

Print all the possible unique original messages in lexicographical order

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/another-problem-2c89443c/
