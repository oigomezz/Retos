t = int(input())
while t > 0:
    n = int(input())
    old = [0] * (n + 1)
    cold = [0] * (n + 1)
    temp = list(map(int, input().split()))
    for i in range(1, n + 1):
        old[i] = old[i - 1]
        cold[i] = cold[i - 1]
        if temp[i-1] & 1:
            if temp[i-1] == 1:
                old[i] += 1
            else:
                cold[i] += 1
        else:
            old[i] += 1

    q = int(input())
    for _ in range(q):
        l, r = map(int, input().split())
        o = old[r] - old[l - 1]
        c = cold[r] - cold[l - 1]
        tot = o - c
        if tot < 0:
            tot = -tot
            print((tot + 1) // 2)
        else:
            print(0)

    t -= 1
