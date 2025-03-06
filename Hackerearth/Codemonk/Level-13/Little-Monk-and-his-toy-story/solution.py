l = int(input())
s = list(map(int, input().split(" ")))
for n in range(1, l):
    if (n*(n+1) > 2*l):
        break

if l > 1:
    print(n-1)
if l == 1:
    print(1)
