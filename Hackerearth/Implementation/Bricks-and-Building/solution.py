n = int(input())
buildings = [0] * n
for i in range(n):
    a = int(input())
    buildings[i] = a

queries = {}
q = int(input())
for i in range(q):
    count = 0
    k = int(input())
    if (k in queries):
        count = queries[k]
    else :
        for j in range(n):
            if buildings[j] % k == 0:
                count += 1
        queries[k] = count
    print(count)
