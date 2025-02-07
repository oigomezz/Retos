# [Hard job][link]

You are given a permutation of integers from 1 to N (very unusual :D). The only thing you should do is to process M queries. Each query has 2 parameters: number X from 1 to N and lowercase latin letter Y (either 'l' or 'r'). You do the following:

1. Calculate distances from the position of the number X to the left end and to the right end of the permutation. Let's call minimum of them accessibleness.
2. Erase number X from it's current position. If parameter Y is 'l' then insert X the very beginning of the permutation. Otherwise insert X after the last element of the permutation.

Please find sum of accessibleness over all queries.

## Input format

- The first line contains two space-separated integers: N and M.
- The second line contains N space-separated integers: the initial permutation.
- After this M lines follow containing 2 space-separated parameters each in the way it's described in the statement above.

## Output format

Output one number - answer for the question.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/hard-job/
