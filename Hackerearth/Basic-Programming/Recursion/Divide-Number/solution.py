t = int(input())
results = []

for _ in range(1, t + 1):
    n = int(input())
    if n % 2 == 1 or n < 4:
        results.append("-1")
    elif n % 4 == 0:
        results.append(str((n // 4) ** 4))
    elif n % 6 == 0:
        results.append(str((n // 6) ** 2 * (n // 3) ** 2))
    elif n % 10 == 0:
        results.append(str((n // 10) * (n // 5) ** 2 * (n // 2)))
    else:
        results.append("-1")

print("\n".join(results))
