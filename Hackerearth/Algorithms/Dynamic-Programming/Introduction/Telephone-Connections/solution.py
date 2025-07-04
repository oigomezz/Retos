def MinMax(A, B):
    x = A // B + 1
    kmin = ((x * (x - 1)) // 2) * (A % B)
    x -= 1
    kmin += ((x * (x - 1)) // 2) * (B - (A % B))
    x = A - B + 1
    kmax = (x * (x - 1)) // 2
    return kmin, kmax


A = int(input())
B = int(input())

out_ = MinMax(A, B)
print(' '.join(map(str, out_)))
