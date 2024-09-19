def similar_elements_pairs(a, n):
    arr = sorted(a)
    is_similar = False
    total = count = 0
    j = arr[0]
    for i in arr:
        if i == j:
            count += 1
        elif j + 1 == i:
            count += 1
            is_similar = True
        else:
            if is_similar:
                total += (count * (count - 1)) // 2
                is_similar = False
            count = 1
        j = i
    if is_similar:
        total += (count * (count - 1)) // 2
    return total


N = int(input())
A = list(map(int, input().strip().split()))
out_ = similar_elements_pairs(A, N)
print(out_)
