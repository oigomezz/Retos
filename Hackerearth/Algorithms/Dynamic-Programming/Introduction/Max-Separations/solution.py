def max_separations(n, k, array):
    odd = even = 0
    separation = []
    for i in range(n - 1):
        if array[i] % 2:
            odd += 1
        else:
            even += 1
        if odd == even:
            separation.append(abs(array[i] - array[i + 1]))
    separation.sort()
    total = i = 0
    length = min(k, len(separation))
    while i < length:
        if total + separation[i] <= k:
            total += separation[i]
            i += 1
        else:
            break
    return i


N = int(input())
K = int(input())
arr = list(map(int, input().split()))

out_ = max_separations(N, K, arr)
print(out_)
