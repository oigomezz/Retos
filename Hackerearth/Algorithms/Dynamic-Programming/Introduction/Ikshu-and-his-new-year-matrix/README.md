# [Ikshu and his new year matrix][link]

Ikshu is in love with prime numbers. He has a matrix of size N X N and wants atleast 5 prime numbers in that matrix arranged like a cross as shown in figure. Let us call this matrix "new year matrix"

    X   X
      X
    X   X

If matrix is not a "new year matrix" he can alter it with the operation as described below:

1. Choose an element from the matrix.
2. Increment the value at the element by K assuring that value of element does not exceed 10000.

Above operation can be applied any number of times.

## Input format

- First line on input contains two integer N and K which is the size of the matrix.
- Followed by N X N matrix. N is the size of the matrix and K is the value which is allowed to be add to any element of matrix.

## Output format

PFirst line of output contains "yes" if such cross is possible else it contains "no". If answer is possible, second line contains the minimum number of operations and third line contains the co-ordinate of center of cross(assuming indexing to be 1-based) If many such answers are possible, print the one with minimum row index, if many answers are possible with same minimum row index print the one with minimum col index.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/ikshu-and-his-new-year-matrix/
