def prime(p):
    flag = True
    if p == 1 or p == 0:
        return False
    for i in range(2, p//2):
        if (p % i == 0):
            flag = False
            break
    return flag


n = int(input())
a = []
for i in range(n):
    temp = list(map(int, input().split()))
    a.append(temp)

pa = []
c = 0
for i in range(n):
    for j in range(n):
        ele = a[i][j]
        s = 0
        if i != 0:
            s += a[i-1][j]
        if i < n-1:
            s += a[i+1][j]
        if j != 0:
            s += a[i][j-1]
        if j < n-1:
            s += a[i][j+1]
        if s in pa:
            c += 1
        else:
            if (prime(s)):
                pa.append(s)
                c += 1

print(c)
