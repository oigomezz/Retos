# Queries and attributes

You are given the following:

- An array A of length n that contains integers.
- DP of length n.
- Arrays L and R of length n that contains integers.

Also, you are given with the following attributes:

- if i = 1, then Li=Ri=1.
- if 2 <= i <= n, 1 <= Li <= Ri < i.
- DP1 = A1.
- DPi = min(DP[Li, Ri]) + Ai.

You are given q queries that state the following:

- You are given two integers x and y.
- You are required to replace DP[1,x] to y and then, update the remaining part of DP. Now, print DPn.

Note:

- You must repeat this task every time you are given these two integers.
- The queries are independent of each other. Therefore, the current query cannot modify the next query.
