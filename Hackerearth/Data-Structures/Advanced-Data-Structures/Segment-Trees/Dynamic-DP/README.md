# Dynamic DP

You are given the following:

- An array A of length n that contains integers
- DP of length n
- Arrays L and R of length n that contain integers

You are also provided with the following attributes:

- If i = 1, then Li = Ri = 1.
- If 2 <= i <= n, then 1 <= Li <= Ri < i
- DP1 = A1
- DPi = min(DP[Li,Ri]) + Ai

The element A[x,y] is defined to be all the elements that are available in [a,b] of array A. For example, DP[2,3] indicates DP2 and DP3.

You are also provided with Q queries that state the following:

- You are given two integers x and y.
- You are required to replace DP[1,x] to y and then update the remaining part of DP. Now, print DPn.

## Note

- You must repeat this task every time you are given these two integers.
- The queries are independent of each other. Therefore, the current query cannot modify the next query.
