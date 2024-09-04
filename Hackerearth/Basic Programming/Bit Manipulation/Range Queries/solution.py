count_array = [[0] * 20 for _ in range(100001)]
for i in range(1, 100001):
    for j in range(20):
        count_array[i][j] = count_array[i - 1][j] + ((i & (1 << j)) != 0)

q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    print(count_array[r][x - 1] - count_array[l - 1][x - 1])
