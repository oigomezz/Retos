import numpy as np

n, m = map(int, input().split())

chessboard = np.zeros((n, m), dtype=int)

for i in range(n):
    chessboard[i] = list(map(int, input().split()))

max_sum = 0
row = -1
col = -1

for i in range(n):
    for j in range(m):
        sum_row = np.sum(chessboard[i]) - chessboard[i][j]
        sum_col = np.sum(chessboard[:, j]) - chessboard[i][j]
        total_sum = sum_row + sum_col
        if total_sum > max_sum or (total_sum == max_sum and (row == -1 or i < row or (i == row and j < col))):
            max_sum = total_sum
            row = i
            col = j

print(f"{row + 1} {col + 1}")

