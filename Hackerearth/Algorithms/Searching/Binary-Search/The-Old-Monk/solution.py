tc = int(input())
for _ in range(tc):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    if a[0] <= b[-1]:
        print(0)
        continue
    monkiness = 0
    i = 0
    for j in range(n):
        if j >= i and b[j] >= a[i]:
            monkiness = max(monkiness, j - i)
        else:
            i += 1
            if i == n:
                break
    print(monkiness)
