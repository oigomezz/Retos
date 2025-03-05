from collections import defaultdict
from heapq import heappush, heappop

al = defaultdict(int)
al = defaultdict(int)
mini = []
maxa = []
m = int(input())
for i in range(m):
    z = list(map(str, input().split()))
    if (z[0] == 'Push'):
        z[1] = int(z[1])
        al[z[1]] += 1
        heappush(mini, z[1])
        heappush(maxa, -z[1])
    if (z[0] == 'CountHigh'):
        while (len(maxa) and al[abs(maxa[0])] == 0):
            heappop(maxa)
        if (len(maxa) == 0):
            print(-1)
        else:
            print(al[abs(maxa[0])])
    if (z[0] == 'CountLow'):

        while (len(mini) and al[abs(mini[0])] == 0):
            heappop(mini)

        if (len(mini) == 0):
            print(-1)
        else:
            print(al[abs(mini[0])])
    if (z[0] == 'Diff'):
        while (len(mini) and al[abs(mini[0])] == 0):
            heappop(mini)
        while (len(maxa) and al[abs(maxa[0])] == 0):
            heappop(maxa)
        if (len(mini) == 0 or len(maxa) == 0):
            print(-1)

        else:
            r = abs(maxa[0])-mini[0]
            print(r)
            if (mini[0] == abs(maxa[0])):
                al[mini[0]] -= 1
            else:
                al[mini[0]] -= 1
                al[abs(maxa[0])] -= 1

            heappush(mini, r)
            heappush(maxa, -r)
