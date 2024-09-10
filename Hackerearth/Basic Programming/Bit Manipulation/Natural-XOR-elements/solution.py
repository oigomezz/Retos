t = int(input())
results = []

for _ in range(t):
    n = int(input())
    x = n % 4

    if x == 0:
        results.append(f"1 {n}")
    elif x == 1:
        results.append("1 1")
    elif x == 2:
        results.append(f"2 {n} 1")
    else:
        results.append("0")

print("\n".join(results))
