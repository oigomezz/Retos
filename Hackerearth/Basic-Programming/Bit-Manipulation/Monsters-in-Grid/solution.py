MX = 20
arr = [[0] * MX for _ in range(MX)]
n, m, k = map(int, input().split())
for i in range(n):
    arr[i] = list(map(int, input().split()))

result = 0
for i in range(1 << m):
    mx_list = [0] * n
    l = k - bin(i).count('1')
    if l < 0:
        continue
    for a in range(n):
        for b in range(m):
            if (i >> b) & 1 and arr[a][b] == 1:
                mx_list[a] += 1
    mx_list.sort(reverse=True)
    result = max(result, sum(mx_list[:min(l, n)]))

print(result)
