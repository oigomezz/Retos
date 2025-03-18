# [Maximum work][link]

Bob has N workers working under him. The ith worker has some strength Wi. Currently, he has M tasks pending with him. Each task can be assigned to only 1 worker. To do particular task i, Strength Si is required i.e. a task i can be done by a worker only if his strength is greater or equal to Si. Bob has K magical pills, taking a magical pill will increase the strength of a worker by B units. Bob gives pills to workers optimally such that the maximum number of tasks can be done.

**Task:** Determine the maximum number of tasks that can be completed.

**Note:** 1-based indexing is followed.

## Function description

Complete the solve function provided in the editor. This function takes the following 6 parameters and returns an integer:

- K: Represents the number of magical pills
- B: Represents an integer denoting the amount of strength that will be increased by taking a pill
- N: Represents the number of workers
- W: Represents an array of integers denoting the strength of the workers
- M: Represents the number of tasks
- S: Represents an array of integers denoting strength required for the task

## Input format

**Note:** This is the input format that you must use to provide custom input (available above the Compile and Test button).

- The first line contains an integer T denoting the number of test cases. T also denotes the number of times you have to run the solve function on a different set of inputs.
- For each test case:
  - The first line contains two space-separated integers K and B.
  - The second line contains an integer N denoting the number of workers.
  - The third line contains N space-separated integers denoting an array W where W[i] represents the strength of the ith worker.
  - The fourth line contains an integer M denoting the number of tasks.
  - The fifth line contains M space-separated integers denoting an array S. S[i] represents the strength required to do the ith task.

## Output format

For each test case in a new line, print the answer representing the maximum number of tasks that can be done.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/maximum-work-11cfd424/
