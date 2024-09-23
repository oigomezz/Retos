T = int(input())
for t in range(T):
    n = int(input())
    k = list(map(int, input().split()))
    dic = {}
    total = 0

    for i in range(len(k)):
        if k[i] in dic:
            total += i-dic[k[i]]
            dic[k[i]] = i
        else:
            dic[k[i]] = i

    print(total)
