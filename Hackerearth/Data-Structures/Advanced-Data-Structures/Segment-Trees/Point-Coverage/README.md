# Point Coverage

There are N points located on the X axis at positions A1,A2,...,An respectively. Alice performs (N - 1) journeys. During the ith journey (1 <= i <= N-1), Alice moves from ith point to (i+1)th point (i.e from position Ai to position Ai+1).

You have to answer Q queries of the following form:

- Li,Ri,Xi (1 <= Li <= Ri <= N-1): How many times does Alice go over point Xi during Li to Ri journey?

## Input format

- The first line of input contains N denoting the number of points on X-axis and Q denoting the number of queries.
- The second line contains N integers A1,A2,...,An denoting the positions of the points on the X axis.
- Q lines follow. The ith of these lines contains three integers Li, Ri, Xi.

## Output format

For each query, print the answer in a separate line.
