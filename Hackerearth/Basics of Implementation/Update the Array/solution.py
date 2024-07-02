def min_updates(n, arr, k):
    if n % 2 != 0:
        return -1

    odd = [x for x in arr if x % 2 != 0]
    set_odd = set(odd)
    size_odd = len(set_odd)

    even = [x for x in arr if x % 2 == 0]
    set_even = set(even)
    size_even = len(set_even)

    odd_k = [x for x in range(1, k+1, 1) if x % 2 != 0 and x not in odd]
    even_k = [x for x in range(1, k+1, 1) if x % 2 == 0 and x not in even]
    count = 0

    if size_odd > size_even and (size_odd - size_even) <= len(even_k):
        count += size_odd - size_even
    elif size_odd < size_even and (size_even - size_odd) <= len(odd_k):
        count += size_even - size_odd
    else:
        count = -1
    return count


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())

    out_ = min_updates(N, A, K)
    print(out_)
