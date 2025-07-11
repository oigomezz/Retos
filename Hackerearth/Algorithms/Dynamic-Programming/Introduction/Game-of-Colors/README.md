# [Game of Colors][link]

You are given a grid of size N\*N where each cell contains either red(R), green(G) or blue(B) color. Each cell changes it color after a fix interval of time t[i] [j] (1<=i,j<=N) known as frequency of that cell.

For example, consider a cell with color R at t=0 and frequency of this cell is 2. At t=1, its colour will be R, at t=2, its colour will be G at t=4 it will be B and at t=6 it will R again. That is, it changes its colour every 2 seconds.

Now you have to answer Q queries where each query contains a time instant T and a sub-grid denoted by Left-top point (x1,y1) and Right-bottom point (x2,y2) and a color C (R,G or B). You have to tell number of cells having color C in the sub-grid at time T.

## Input format

- First line : Two space separated integers N and Q.
- Next N lines : N space separated integers denoting frequency of each cell
- Next Q lines : Five space separated integers and a space separated characted C denoting T x1 y1 x2 y2 C where C is the color.

## Output format

For each test case output desired answer in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/game-of-colors/
