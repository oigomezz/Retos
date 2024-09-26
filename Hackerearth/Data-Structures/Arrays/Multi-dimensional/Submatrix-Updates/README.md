# Submatrix Updates

You will be given a N x M matrix A of integers and K add operations to execute. An add operation adds a constant to all of the entries in a square sub-matrix of A and it is specified by 4 integers R, C, S and D where R is the row number, C is the column number, S is the size of the sub-matrix and D is the constant to add to the entries. The entry at row R and column C is denoted by A [R] [C]. The row and column numbers in a query correspond to the upper-left corner of the square sub-matrix to update.

Your task it to print the matrix after applying all of the K add operations.

## Input format

The first line of input contains three numbers N, M, K representing the number of rows, the number of columns and the number of add operations respectively. N lines follow each containing M space-separated integers. K lines follow each containing four numbers R, C, S and D as described above.

## Output format

Print the matrix after applying all of the K add operations. The matrix should be printed on N lines each containing M space-separated integers.
