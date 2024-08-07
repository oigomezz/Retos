import math
t = int(input())
for z in range(t):
    t0, t1, t2, v1, v2, d = map(int, input().split())
    if (t0 > t1 and t0 > t2):
        print(-1)
    else:
        if (t0 > t2):
            t11 = math.ceil((d/v1)*60 + t1)
            print(int(t11))
        elif (t0 > t1):
            t12 = math.ceil((d/v2)*60 + t2)
            print(int(t12))
        else:
            t11 = math.ceil((d/v1)*60 + t1)
            t12 = math.ceil((d/v2)*60 + t2)
            print(int(min(t11, t12)))
