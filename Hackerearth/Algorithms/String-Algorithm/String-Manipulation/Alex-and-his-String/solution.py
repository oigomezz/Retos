from heapq import heapreplace, heappop, heapify


def Solve(S, K):
    x = ''
    temp = list(S[:K])
    heapify(temp)
    for c in S[K:]:
        x += heapreplace(temp, c)
    while temp:
        x += heappop(temp)
    return x


S = input()
K = int(input())
out_ = Solve(S, K)
print(out_)
