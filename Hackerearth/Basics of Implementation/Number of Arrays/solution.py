def check(mini, q):
    if (mini < q):
        return mini
    return "NO"


t = int(input())
for _ in range(t):
    n, k, q = map(int, input().split())
    l = list(map(int, input().split()))

    if (k > 2):
        print(check(min(l), q))
    elif (k == 1 or n == 1):
        print(check(max(l), q))
    else:
        print(check(min(l[0], max(l[1: n]), l[-1]), q))
