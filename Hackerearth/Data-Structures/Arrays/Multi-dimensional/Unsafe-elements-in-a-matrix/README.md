# Unsafe elements in a matrix

You have a matrix S consisting of N rows and M columns. Let u be the maximum element of the matrix and v be the smallest element of the matrix. If any element whose value is equal to u or v are called unsafe elements and they disfigure the complete row and column of the matrix. More formally, if any element is equal to u or v and contains cell number (x,y), that is, S [x] [y] = u or S [x] [y] = v are unsafe so that they also disfigure all the cells that have row x or column y and also are unsafe.

Your task is to find the number of safe elements.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case consists of two space-separated integers N and M.
- Next N lines consist of M space-separated integers.

## Output format

For each test case, print a single integer denoting the safe elements.
