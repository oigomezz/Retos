def traversal(ele):
    lesser = 0
    greater = 0
    for i in l:
        if i < ele:
            lesser += i
        elif i > ele:
            greater += i
    if lesser == greater:
        return 0
    return 1 if lesser > greater else 2


n = int(input())
l = list(map(int, input().split()))
low = min(l)
high = max(l)
while low < high:
    m = (low + high)//2
    flag = traversal(m)
    if not flag:
        print("YES")
        break
    elif (flag == 1):
        high = m
    else:
        low = m + 1
else:
    print('NO')
