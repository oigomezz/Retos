T = int(input())

for _ in range(0, T):
    arr = list(map(int, input().split()))
    N = arr[0]
    M = arr[1]
    K = arr[2]
    s = 0

    if N % K == 0:
        s = s+(N//K)
    else:
        s = s+(N//K)+1
    if M % K == 0:
        s = s+(M//K)
    else:
        s = s+(M//K)+1

    print(s)
