import math
a, b = map(int, input().split())
l, r = map(int, input().split())
k = int(input())
x = a % b
if a < b:
    if l <= a + 1:
        res = r - a
    else:
        res = r - l + 1
    if b >= l and b <= r:
        res -= 1
    if res < 0:
        res = 0
    print(res)
    if res > k:
        print(-1)
    else:
        for i in range(a + 1, r+1):
            if i != b:
                print(str(i))

else:
    st = 1
    end = r
    if r > math.floor(math.sqrt(a - x)):
        end = int(math.floor(math.sqrt(a-x)))
    res = []
    res1 = []
    if st == end + 1 and (a-x) % st == 0:
        res.append(st)
    for i in range(st, end + 1):
        if (a - x) % i == 0 and i >= l and i <= r and i != b and i > x:
            res.append(i)
        if (a-x) % i == 0 and (a-x)//i >= l and (a-x)//i <= r and (a-x)//i != b and (a-x)//i >= x and (a-x)//i != end:
            res1 = [(a-x)//i] + res1
    res = res + res1
    print(len(res))
    if len(res) >= k:
        print(-1)
    else:
        for v in res:
            print(str(v))
