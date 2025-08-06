n = int(input())
speeds = list(map(int, input().strip().split()))
a = [speeds[0]]
b = [0] * n
for i in range(1, n):
    if speeds[i] <= a[-1]:
        a.append(speeds[i])
    else:
        j = i - 1
        mx = 0
        while j >= 0:
            if speeds[j] >= speeds[i]:
                mx = max(mx, b[j])
            j -= 1
        b[i] = mx + 1
print(len(a) + max(b))
