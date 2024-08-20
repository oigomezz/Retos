t = int(input())
for _ in range(t):
    n = int(input())
    goldens = silvers = bronces = 0
    for i in range(n):
        arr = list(map(int, input().split()))
        goldens += arr[0]
        silvers += arr[1]
        bronces += arr[2]
    print(max(goldens, silvers, bronces))
