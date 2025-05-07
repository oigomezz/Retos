# [Process Scheduling][link]

Note: This is an approximate problem. There is no exact solution. You must find the most optimal solution. Please, take a look at the sample explanation to ensure that you understand the problem correctly.

Given a CPU which can work for W minutes and can handle one process at a time.

N process are given with their benefit value B[i], run time R[i] (in minutes) and deadline D[i] (in minutes). All process are available from time T = 0.

Find a subset of N processes and their order for execution, with maximum possible sum of benefit value. They should be handled by CPU without collision and satisfying their deadlines.

The goal is to maximize Z = Σ B[j]

## Note

- R[i] for a process can also be greater than W.
- CPU will start the process immediately once that will available.
- You can use some process atmost once.
- Process can't be under execution beyond deadline.

## Input format

- First line contains W, denoting time for which CPU works.
- Next line contain N, denoting number of processes available.
- Next N lines contain 3 integers B[i] R[i] D[i], parameters corresponding to the i-th process.

## Output format

- Print X the size of the subset selected.
- In the next line, print X space separated integers, denoting the processes in the order that are handled by CPU.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/approximate/process-scheduling-34fa1bb3/
