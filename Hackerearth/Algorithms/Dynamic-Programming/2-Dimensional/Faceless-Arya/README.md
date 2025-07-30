# [Faceless Arya][link]

The story revolves around the famous Arya Stark of Game of Thrones, popularly known as the Faceless Arya. After killing Lord Walder of House Frey and his sons, Arya decides to return home to Winterfell.

The path from House Frey to Winterfell can be described as a N \* M matrix A consisting of N rows numbered from 1 to N and M columns numbered from 1 to M where each of the cells has some points. Aij denotes the points of the cell in the i-th row and j-th column. As we all know, Arya is very greedy and she wants to collect the maximum sum of points that she can while returning home. She can move from any cell (i,j) to (i+1, k) if and only if GCD(Aij,Ai+1k) != 1 where GCD(X,Y) is the greatest common divisor of X and Y. House Frey is at row 1 of the matrix A and Winterfell is at row N. Output the maximum sum of points that she can achieve.

## Input format

- The first line of input contains a single integer T denoting the number of test cases.
- The first line of each test case contains 2 space separated integers N and M denoting the number of rows and number of columns of the matrix A respectively.
- Each of the next N lines contain M space separated integers describing the matrix A.

## Output format

For each test case, print an integer in a new line denoting the answer for that test case. If there is no way to reach Winterfell, then output 0.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/faceless-arya-67489283/
