# Minimum Maximum Plants

Consider a garden represented as an n x m grid, where each unit cell has dimensions of 1 x 1 and contains a pot. The rows are numbered from 0 to n-1 from top to bottom. The columns are numbered from 0 to m-1 from left to right. Some of these pots within the garden have been broken. The objective is:

1. Determine the maximum number of plants that can be strategically planted in the garden, adhering to the constraint that no two plants can be consecutively planted in the same row, where consecutiveness implies being placed in adjacent columns.
2. Identify the minimum number of plants required to effectively cover the garden while ensuring that no additional plants can be accommodated without violating the non-consecutive planting rule.

We denote the cell on the ith (0 <= i <= n-1) row and jth (0 <= j <= m-1) column by (i,j).

## Input format

- The first line contains two space-separated integers, n and m, representing the dimensions of the garden.
- The second line contains an integer b, representing the number of broken pots in the garden.
- The next b lines each contain space-separated integers i and j, representing the cells (i,j) where the pots are broken.
- In input a particular cell (i,j) can be present more than once.

## Output format

In a new line print 2 space-separated integers representing the maximum number of plants that can be strategically planted and the minimum number of plants required for effective coverage, respectively.
