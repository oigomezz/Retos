t = int(input())
while (t != 0):
    num = []
    s = input()
    ds = set(s)
    if (len(ds) == 26):
        print("YES")
    else:
        print("NO")
    t = t-1
