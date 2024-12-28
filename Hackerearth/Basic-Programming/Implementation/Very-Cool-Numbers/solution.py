t = int(input())
for _ in range(t):
    r, k = map(int, input().split())
    cool = 0

    for n in range(5, r + 1):
        i = n
        it = 0
        count = 0
        arr = []

        while i != 0:
            arr.append(i & 1)
            i >>= 1
            it += 1

        for k in range(it - 1, 1, -1):
            if arr[k] == 1 and arr[k - 1] == 0 and arr[k - 2] == 1:
                count += 1

        if count >= k:
            cool += 1

    print(cool)
