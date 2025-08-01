# [Decreasing Paths][link]

The end semester exams are now approaching. Ritu is the Computer Science Teacher of Coder Public School. He has been assigned the task of preparing good algorithmic problems for the students by the Dean of the school.

Ritu like every other teacher has his own favorite topics. Ritu likes matrices and maths. So, he tries to create a problem that contains a mixture of both the things. After thinking for weeks, he comes up with a really awesome problem to blow away the minds of his students. But, before giving this problem in the exam he wants to check whether it's tough for his students or not. So, he gives his problem to you to solve so that he could decide whether his problem is good enough or not. So here goes the problem:

Given an N\*N matrix where each cell in the matrix contains number between 1 to 100. The students are required to report the total number of decreasing paths.

From a particular cell (x,y) you can only go to cells (x+1,y) , (x-1,y) , (x,y+1) , (x,y-1) but you can't go outside the matrix, and you can't go to cell with higher or equal number than the number in current cell.

Since the number of such paths could be huge he asks them to tell him modulo 10⁹ + 7. A path of only one cell is counted as a path.

So try your hand on Ritu's problem and give him a feedback on his problem so that he could decide whether his problem was good enough or not.

## Input format

- The first line contains the integer N denoting the size of matrix.
- This is followed by N lines where each line contains N space separated integers.

## Output format

Print the total number of such paths Modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/decreasing-paths/
