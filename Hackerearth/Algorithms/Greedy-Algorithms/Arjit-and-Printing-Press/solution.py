t = int(input())
for _ in range(t):
    w = list(input())
    r = list(input())
    r.sort()
    left = 0
    for i in range(len(w)):
        if left < len(r) and ord(w[i]) > ord(r[left]):
            w[i] = r[left]
            left += 1

    print(''.join(w))
