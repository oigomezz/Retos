T = int(input())
for i in range(T):
    N = int(input())
    A = [x for x in input().split()]
    number = "".join(A)
    B = [x for x in number]
    B.sort(reverse=True)
    res = "".join(B)
    print(res)
