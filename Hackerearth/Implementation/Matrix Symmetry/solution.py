t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        m = list(input())
        arr.append(m)
    m = n//2
    tag_h = 0
    for i in range(m):
        if arr[i] != arr[n-i-1]:
            tag_h = 1
            break
    tag_v = 0
    m = len(arr)//2
    n = len(arr)-1
    for k in range(m):
        for i in range(len(arr)):
            if arr[i][k] != arr[i][n-k]:
                tag_v = 1
    if tag_h == 0 and tag_v == 0:
        print("BOTH")
    if tag_h == 1 and tag_v == 0:
        print("VERTICAL")
    if tag_h == 0 and tag_v == 1:
        print("HORIZONTAL")
    if tag_h == 1 and tag_v == 1:
        print("NO")
