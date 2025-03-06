n = int(input())
bs = list(map(int, input().split()))
bs.sort()
ks = list(map(int, input().split()))
ks.sort()
su = 0
for i in range(n):
    su += (abs(bs[i]-ks[i]))
print(su)
