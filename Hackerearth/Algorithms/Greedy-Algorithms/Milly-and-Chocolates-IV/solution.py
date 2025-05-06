t = int(input())
for _ in range(t):
    n, k, m = map(int, input().strip().split())
    p = list(map(int, input().strip().split()))
    min_eat_time = float('inf')
    index = 0
    for i in range(n):
        time = map(int, input().strip().split())
        eat_time = p[i] * k + sum(time) + (p[i] - 1) * m
        if eat_time < min_eat_time:
            min_eat_time = eat_time
            index = i
    print(index + 1, min_eat_time)
