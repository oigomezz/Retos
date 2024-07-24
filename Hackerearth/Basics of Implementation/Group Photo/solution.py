n = int(input())
w = [0] * n
h = [0] * n

for i in range(n):
    w[i], h[i] = map(int, input().split())

sum_w = sum(w)
temp = h[:]
temp.sort(reverse=True)

max1 = temp[0]
max2 = temp[1]

results = []
for i in range(n):
    ans1 = sum_w - w[i]
    if h[i] != max1:
        ans2 = max1
    else:
        ans2 = max2
    results.append(ans1 * ans2)

print(" ".join(map(str, results)))
