# Roy and Symmetric Logos

Roy likes Symmetric Logos.

How to check whether a logo is symmetric?
Align the center of logo with the origin of Cartesian plane. Now if the colored pixels of the logo are symmetric about both X-axis and Y-axis, then the logo is symmetric.

You are given a binary matrix of size N x N which represents the pixels of a logo.
1 indicates that the pixel is colored and 0 indicates no color.

For instance: Take a 5x5 matrix as follows:

    01110
    01010
    10001
    01010
    01110

Observe that it is symmetric about both X-axis and Y-axis.

Let's take another example of 5x5 matrix:

    00100
    01010
    10001
    01010
    01110

Now this logo is symmetric about Y-axis but it is not symmetric about X-axis.

Your task is to output YES if the logo is symmetric else output NO.

## Input format

- First line contains T - number of test cases.
- T test cases follow:
  - First line of each test case contains the N - size of matrix.
  - Next N lines contains binary strings of length N.

## Output format

Print YES or NO in a new line for each test case.
