HH, c, n = map(int, input().split())
crew = []
for _ in range(c):
    crew.append(list(map(int, input().split())))
maxHeight = max(crew)[0]
for i in range(n):
    height, time = map(int, input().split())
    if height > maxHeight:
        print("YES")
    else:
        ans = "YES"
        for m in crew:
            if m[1] <= time <= m[2] and m[0] >= height:
                ans = "NO"
                break
        print(ans)
