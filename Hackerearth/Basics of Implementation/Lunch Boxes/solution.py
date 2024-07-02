T = int(input())

for _ in range(T):
    s = 0
    count = 0
    N, M = map(int, input().split())
    A = [int(x) for x in input().split()]
    order_list_A = sorted(A)
    for k in range(M):
        s += order_list_A[k]
        if order_list_A[k] < N and s <= N:
            count += 1
    print(count)
