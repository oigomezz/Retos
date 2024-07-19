def can_be_equal(a, b, n):
    A = []
    B = []

    for i in range(n):
        if a[i] != b[i]:
            A.append(a[i])
            B.append(b[i])

    if len(A) == len(B) == 0:
        return True

    if len(A) == len(B) == 2 and A[0] == A[1] and B[0] == B[1]:
        return True

    return False


T = int(input())
while T > 0:
    n = int(input())
    s = input().split()
    t = input().split()

    if can_be_equal(s[0], t[0], n):
        print("YES")
    else:
        print("NO")

    T -= 1
