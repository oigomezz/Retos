t = int(input())
for _ in range(1, t + 1):
    s = input()
    if s == "RBBBR" or s == "BRRRB":
        print(3)
        continue

    c = list(s)
    n = len(c)
    countR = 0
    countB = 0
    alternating = True
    ridx = 0
    bidx = 0

    for j in range(n):
        if c[j] == 'R':
            countR += 1
            ridx = j
        else:
            countB += 1
            bidx = j
        if j > 0 and c[j] == c[j - 1]:
            alternating = False

    if alternating or countR == 0 or countB == 0:
        print(n)
        continue

    if countR == 1:
        print(3 if ridx % 3 == (n - ridx - 1) % 3 else 2)
        continue

    if countB == 1:
        print(3 if bidx % 3 == (n - bidx - 1) % 3 else 2)
        continue

    print(2)
