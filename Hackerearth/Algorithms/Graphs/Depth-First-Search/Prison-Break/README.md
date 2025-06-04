# [Prison Break][link]

Alfie was a prisoner in mythland. Though Alfie was a witty and intelligent guy.He was confident of escaping prison.After few days of observation,He figured out that the prison consists of (N\*N) cells.i.e The shape of prison was (N\*N) matrix. Few of the cells of the prison contained motion detectors.So Alfie planned that while escaping the prison he will avoid those cells containing motion detectors.Yet before executing his plan,Alfie wants to know the total number of unique possible paths which he can take to escape the prison.Initially Alfie is in cell (1,1) while the exit of the cell (N,N).

**Note:** -> Alfie can move in all four direction{ if his current location is (X,Y), he can move to either
(X+1,Y), (X-1,Y), (X,Y+1), (X,Y-1) }. If the first cell (1,1) and the last cell(N,N) contain motion detectors,then Alfie can't break out of the prison.

## Input format

- The first line contain number of test cases "T".
- T test cases follow:
  - The first line of each test case contains an integer "N",(i.e the size of the (N\*N) matrix).
  - The next n lines contain N space separated values either 0 or 1."1" represents a cell containing motion detectors.

## Output format

Output total number of unique possible paths which he can take to escape the prison.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/prison-break-5/
