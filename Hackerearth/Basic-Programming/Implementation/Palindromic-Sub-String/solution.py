from itertools import combinations
list1 = []
s1 = input()
res1 = [(s1[x:y]) for x, y in combinations(range(len(s1) + 1), r=2)]
for j in res1:
    if str(j[::-1]) in res1 and len(j) > 1 and j not in list1:
        list1.append(len(j))
if list1 != []:
    print('YES')
    print(max(set(list1)))
else:
    print('NO')
