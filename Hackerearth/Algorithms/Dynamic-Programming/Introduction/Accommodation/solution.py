m, n = map(int, input().strip().split())
c = list(map(int, input().strip().split()))
accommodation = [0] * (n + 1)
accommodation[0] = 1
for i in c:
    for j in range(i, n + 1):
        accommodation[j] += accommodation[j - i]
        accommodation[j] %= 1000000007
print(accommodation[n])
