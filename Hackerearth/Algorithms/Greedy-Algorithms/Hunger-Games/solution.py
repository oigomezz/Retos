n = int(input())
hunger_values = sorted(map(int, input().strip().split()))
ans = 0
for i in range(n - 2):
    ans = max(ans, hunger_values[i + 2] - hunger_values[i])

print(ans)
