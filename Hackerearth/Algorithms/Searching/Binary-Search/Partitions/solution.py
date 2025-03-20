def get_partitions(arr):
    temp = [0]*n
    for i in reversed(range(n)):
        total = 0
        for j in range(i, n):
            total += arr[j]
            if total > r:
                break
            if total >= l:
                if j == n - 1:
                    temp[i] = (temp[i] + 1) % mod
                else:
                    temp[i] = (temp[i] + temp[j+1]) % mod
    return temp[0]


mod = 10**9 + 7
n, l, r = map(int, input().split())
arr = list(map(int, input().split()))
print(get_partitions(arr))
