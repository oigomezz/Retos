t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    matrix = []
    for _ in range(n):
        matrix.append(input().strip())
    if len(set(matrix)) < n:
        print("No")
    else:
        print("Yes")
