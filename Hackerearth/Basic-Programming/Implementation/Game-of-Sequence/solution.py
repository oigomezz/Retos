def find_the_winner(a):
    if len(set(a)) % 2:
        return 'P'
    else:
        return 'Q'


t = int(input())
for _ in range(t):
    n = int(input())
    A = map(int, input().split())

    out_ = find_the_winner(A)
    print(out_)
