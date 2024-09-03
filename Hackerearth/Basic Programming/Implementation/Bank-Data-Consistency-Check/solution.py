from collections import Counter

x = ()
l = []

while x != (-1, -1):
    x = tuple(map(int, input().split()))
    l.append(x)

l.pop()
counter = Counter(l[0])

for i in l[1:]:
    counter.update(i)

account_no = counter.most_common()[0][0]
for j in l:
    if account_no in j:
        if j[0] == account_no and j[1] != account_no:
            print("0 1")
        if j[0] != account_no and j[1] == account_no:
            print("1 0")
    else:
        print("-1 -1")
