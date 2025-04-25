# [Mosaics and holes][link]

John wants to cover his yard floor with mosaics. The yard floor is a n x m matrix and each cell is either a mosaic or a hole. John has invented a flipper machine. This machine has a size of k and can select a k x k square of the yard and flip the cells in it. By this action, every hole in the square becomes a mosaic and every mosaic in the square becomes a hole.

Help John to cover the floor of the yard completely by mosaics by using this machine. In each step, John selects a k x k square of the yard floor and sets the machine on it. He wants to compute the minimum steps needed to repair the yard floor.

## Input format

- First line: Three integers n,m,k, where n is the number of matrix rows, m as the number of matrix columns, and k as the size of the flipper machine.
- Next n lines: Each line will contain m integer 0 or 1 with space in between the consecutive one.
- This n lines are the data of the yard floor matrix, 1 indicates that the cell is mosaic and 0 indicates that the cell is a hole.

## Output format

Print an integer denoting the minimum number of steps needed to repair the yard floor or -1 if it is impossible to repair the yard floor with this machine.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/filip-kotinioo-39795217/
