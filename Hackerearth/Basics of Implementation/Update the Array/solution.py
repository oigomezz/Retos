def min_updates(n, arr, k):
    if n % 2 != 0:
        return -1

    count = 0
    arr = set(arr)
    odd = [x for x in arr if x % 2 != 0]
    even = [x for x in arr if x % 2 == 0]

    odd_k = [x for x in range(1, k+1, 1) if x % 2 != 0 and x not in odd]
    even_k = [x for x in range(1, k+1, 1) if x % 2 == 0 and x not in even]

    while len(odd) < n//2:
        if len(odd_k) > 0:
            odd.append(odd_k.pop(0))
            count += 1
        else:
            return -1

    while len(even) < n//2:
        if len(even_k) > 0:
            even.append(even_k.pop(0))
            count += 1
        else:
            return -1

    return count


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = min_updates(N, A, K)
    print(out_)
