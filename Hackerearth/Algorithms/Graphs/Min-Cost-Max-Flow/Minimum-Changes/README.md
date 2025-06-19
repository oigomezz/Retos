# [Minimum changes][link]

You are provided K different tasks and you have to perform a single activity on a single day. The activities are numbered by using the integers [1,2,...,K].

A time table has been provided to you that must be followed for the next N days. The time table states that on the day, you should do the job with index A[i], 1 <= A[i] <= K.

A rule states that if you do some particular job with index X on a day with index Y, then you should not do the same job any time before day Y + K. You cannot perform the job with index X on any day in the range [Y+1, Y + K - 1] in such a case.

You are required to change the time table in such a way that it also satisfies the mentioned rule. You also have to make the minimum number of changes in the time table. A change involves modifying a job that has to be done on some day i (1 <= i <= N) to any other job in the range of 1 ... K. Your task is to determine this minimum number.

## Input format

- First line: Single integer T denoting the number of test cases in a single test file.
- For each test case:
  - First line: Two space-separated integers N and K.
  - Next line: N space-separated integers, where the i-th integer denotes the job that you should do on the i-th next day.

## Output format

For each test case, print a single integer on a single line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/practice-problems/algorithm/mr-x-and-jobs-1-77e795c3/
