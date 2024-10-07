n, k = map(int, input().strip().split())
memory = []
for _ in range(n):
    memory.append(list(map(int, input().strip().split())))
q = int(input())
for _ in range(q):
    x = int(input())
    i = 0
    j = k - 1
    found = 0
    while i < n:
        if memory[i][j] < x:
            i += 1
        elif memory[i][j] > x:
            j -= 1
        else:
            print(i, j)
            break
    else:
        print(-1, -1)
