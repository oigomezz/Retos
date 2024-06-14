T = int(input())
for _ in range(T):
    n = int(input())
    a = input()
    b = input()
    res = 'Yes'
    c = 0
    for i in a:
        if i == '?':
            c += 1
        else:
            if i in b:
                b = b.replace(i, '', 1)
            else:
                res = 'No'
                break
    print(res)
