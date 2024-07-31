t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    m = min(lst)
    s = 0
    for j in lst:
        s += j-1
    print(m-1, s)
