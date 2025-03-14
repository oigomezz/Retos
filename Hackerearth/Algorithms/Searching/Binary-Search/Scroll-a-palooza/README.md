# [Scroll-a-palooza][link]

In a small town, there's a ritual where each day, every resident takes a series of steps, either to the right or left, over N days. Starting at the town center, each day, they move according to the guidance of a mystical scroll: a list of values, X which determines their direction. On the i-th day, a positive X[i] sends them to the right by X[i] steps, a negative X[i] sends them to the left by X[i] steps, and a zero means they stay where they are. Over time, the townsfolk became curious about their wanderings.

They posed M queries, each asking: on which days did residents find themselves at least W steps away from the town center, both for the first time and the last time? If residents are never at least W steps away from the town center, the answer is -1.

## Input format

- The first line contains a single integer T, which denotes the number of test cases.
- For each test case:
  - The first line contains N denoting the number of days.
  - The second line contains N space-separated integers, denoting the values of scroll X.
  - The next line contains M denoting the number of queries.
  - The next M lines contain an integer, denoting W.

## Output format

For each test case, answer all the M queries. For each query, print two days on which residents are at least a W steps away from the town center, the first and last time in a new line. If residents are never at least W steps away from the town center, print in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/scroll-a-palooza-bed5c880/
