k = int(input())
days = sorted(map(int, input().strip().split()), reverse=True)
earliest = -1
for i in range(k):
    base = 1 + i
    evolve = base + days[i]
    earliest = max(earliest, evolve)
print(earliest + 1)
