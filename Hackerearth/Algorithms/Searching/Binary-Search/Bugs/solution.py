import bisect

n = int(input())
li = list()
for i in range(n):
    q = [int(i) for i in input().split()]
    if q[0] == 1:
        if i == 0:
            li.append(q[1])
        else:
            bisect.insort_left(li, q[1])
    else:
        n = len(li)
        if n < 3:
            print("Not enough enemies")
        else:
            print(li[-(n//3)])
