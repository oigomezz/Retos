tc = int(input())
for _ in range(tc):
    n, m = map(int, input().strip().split())
    is_possible = True
    for _ in range(m):
        x, y = map(int, input().strip().split())
        if is_possible and (x == y or (x > n and x > y and x > n + y)):
            is_possible = False
    print('YES' if is_possible else 'NO')
