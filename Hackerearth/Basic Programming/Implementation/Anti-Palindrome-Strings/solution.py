T = int(input())

for _ in range(T):
    s = input()
    if s == s[::-1]:
        print("-1")
    else:
        s = list(s)
        s = sorted(s)
        temp = ("".join(s))
        print(temp)
