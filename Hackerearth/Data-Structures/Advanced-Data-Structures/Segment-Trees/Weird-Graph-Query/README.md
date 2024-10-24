# Weird Graph Query

We are given an connected undirected weighted graph of N nodes and M edges. We are then given Q queries where in each query we are given integers U, L, R, K. For every query we have to report the smallest integer C such that there are at least K nodes x such that L <= x <= R and shortest distance from x to U is not more than C.

## Input format

- The first line contains two integers N,M.
- The next M lines contains three space separated integers a,b,c meaning that there is an edge between nodes a and b of weight c.
- The next line contains an integer Q.
- Q lines follow, each with four integers U, L, R, K with the meaning as given in problem.

## Output format

 Qlines should be printed and the i-th line should contain the output for the i-th query.
