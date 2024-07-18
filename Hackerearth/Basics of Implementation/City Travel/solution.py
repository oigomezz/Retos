import math

s, x, n = map(int, input().split())
distance = []

for _ in range(n):
    t, y = map(int, input().split())
    distance.append([t, y])

distance.sort()
currentday = distance[0][0]
prevday = currentday - 1

currenttravel = prevday * x + distance[0][1]

remaining = s - currenttravel

if remaining < 0:
    days = math.ceil(s / x)
else:
    i = 1

    while i < n:
        prevtravel = currenttravel

        currentday = distance[i][0]
        prevday = currentday - 1
        gapdays = prevday - distance[i-1][0]

        prevtraveltotal = prevtravel + gapdays * x

        currenttravel = prevtraveltotal + distance[i][1]

        remaining = s - currenttravel

        if remaining < 0:
            if (s - prevtraveltotal) < 0:
                gapdays = math.ceil((s - prevtravel) / x)
                days = distance[i-1][0] + gapdays
                break
            else:
                days = distance[i][0]
                break
        i += 1

    if i == n:
        gapdays = math.ceil((s - currenttravel) / x)
        days = distance[i-1][0] + gapdays

print(days)
