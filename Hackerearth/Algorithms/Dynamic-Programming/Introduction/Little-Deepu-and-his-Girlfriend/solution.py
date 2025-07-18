t = int(input())
players = {
    1: 'Kate',
    2: 'Little Deepu',
}
for _ in range(t):
    m, n = map(int, input().strip().split())
    s = list(map(int, input().strip().split()))
    res = [False] * m
    for i in s:
        res[i - 1] = True
    for i in range(m):
        if not res[i]:
            for j in s:
                if i + j < m:
                    res[i + j] = True
    print(players[res[-1] + 1])
