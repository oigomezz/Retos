def minUpdates(N, A, K):
    # write your code here
    pass


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = minUpdates(N, A, K)
    print(out_)
