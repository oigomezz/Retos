n = int(input())
a = list(map(int, input().split()))
s, e = map(int, input().split())
leng = len(a)
for i in range(1, leng+1):
    if s == e:
        print("Yes")
        break
    if a[s-1] == e:
        print("Yes")
        break
    else:
        if i == len(a):
            print("No")
            break
        s = a[s-1]
