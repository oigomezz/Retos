t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    children = []
    for i in range(1, n+1):
        children.append((i, arr[i-1]))
    child = (0, 0)
    while len(children) > 0:
        child = children.pop(0)
        if child[1] > m:
            children.append((child[0], child[1] - m))
    print(child[0])
