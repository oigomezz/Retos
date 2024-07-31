n, m = map(int, input().split())
ans = 1

for i in range(1, m+1):
    ans = (ans*i) % (10**9+7)
print(ans)
