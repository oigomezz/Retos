test = int(input())

for _ in range(test):
    n = int(input())
    curXor = 0
    cnt = [0] * 100
    cnt[0] = 1
    ans = 0
    arr = list(map(int, input().split()))

    for i in range(n):
        x = arr[i]
        curXor ^= x
        parity = bin(curXor).count('1') % 2
        ans += cnt[parity ^ 1]
        cnt[parity] += 1

    print(ans)
