from collections import defaultdict

d, dic, count = defaultdict(list),   defaultdict(list),  1
for _ in range(int(input())):
    name, time = input().split()
    time = int(time)
    if (d[name]):
        d[name][0] += 100
        d[name][1] += time
    else:
        d[name] = [100, time]

for i in d:
    dic[d[i][0]].append([d[i][1],  i])


for i in sorted(dic, reverse=True):
    for j in sorted(dic[i]):
        print(count, j[1])
        count += 1
