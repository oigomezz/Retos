t = int(input())
results = []
for _ in range(t):
    n = int(input())
    bits = [0] * 32
    total = (n * (n - 1)) // 2

    arr = list(map(int, input().split()))
    for i in range(n):
        for j in range(31, -1, -1):
            if arr[i] & (1 << j):
                total -= bits[j]
                bits[j] += 1
                break

    results.append(total)

print("\n".join(map(str, results)))
