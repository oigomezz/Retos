# Disk tower

Your task is to construct a tower in N days by following these conditions:

- Every day you are provided with one disk of distinct size.
- The disk with larger sizes should be placed at the bottom of the tower.
- The disk with smaller sizes should be placed at the top of the tower.

The order in which tower must be constructed is as follows:

- You cannot put a new disk on the top of the tower until all the larger disks that are given to you get placed.

Print N lines denoting the disk sizes that can be put on the tower on the day.

## Input format

- First line: N denoting the total number of disks that are given to you in the N subsequent days.
- Second line: N integers in which the ith integers denote the size of the disks that are given to you on the ith day.

**Note:** All the disk sizes are distinct integers in the range of  1 to N.

## Output format

Print N lines. In the ith line, print the size of disks that can be placed on the top of the tower in descending order of the disk sizes.

If on the ith day no disks can be placed, then leave that line empty.
