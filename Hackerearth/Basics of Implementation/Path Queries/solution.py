t = int(input().strip())
for _ in range(t):
    n, q = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    ec, oc = 0, 0
    for num in a:
        if num % 2 == 0:
            ec += 1
        else:
            oc += 1

    for _ in range(n - 1):
        input()

    result = []
    for _ in range(q):
        index, val = map(int, input().strip().split())
        if a[index - 1] % 2 == 0:
            ec -= 1
        else:
            oc -= 1
        a[index - 1] = val
        if val % 2 == 0:
            ec += 1
        else:
            oc += 1
        r = (ec * (ec + 1) // 2) + (oc * (oc + 1) // 2)
        result.append(str(r))
    print(" ".join(result))
