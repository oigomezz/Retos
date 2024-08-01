T = int(input())
for _ in range(T):
    N = int(input())
    B = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]

    if max(A) == max(B):
        print('Tie')
    elif max(A) > max(B):
        print('Alice')
    else:
        print('Bob')
