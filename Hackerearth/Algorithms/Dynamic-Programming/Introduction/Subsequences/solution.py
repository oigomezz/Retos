q = int(input())
k_list = []
for _ in range(q):
    k = int(input())
    k_list.append(k)
n = max(k_list)
v = 1
dp = [0] * (n + 1)
for i in range(1, n + 1):
    s = str(v)
    if int(s[0]) % 2 == 0:
        v += pow(10, len(s) - 1)
    dp[i] = v
    v += 1
for k in k_list:
    print(1, dp[k])
