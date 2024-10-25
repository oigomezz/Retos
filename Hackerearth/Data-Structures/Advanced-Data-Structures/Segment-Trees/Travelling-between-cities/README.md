# Travelling between cities

You are given positions of N cities situated on X axis. The position of the i-th city is denoted by array value Location[i].You have a bike which can travel atmost K unit distance once the tank is full and each city has a fuel pump. You can assume that once the bike reaches a city its tank is again filled up completely.Now you have to answer Q queries where each query is of the following form.

- L R X: Find the number of cities lying in the index range [L,R] that you can reach from the city at index X.

## Input format

- First line: T i.e Number of testcases.
- For each testcase :
  - First line: Three space separated integers N, K and Q.
  - Second line: N space separated integers denoting the location of cities.
  - Next Q lines : Three space separated L R X integers denoting the query.

## Output format

Output the answer to each query in a separate line.
