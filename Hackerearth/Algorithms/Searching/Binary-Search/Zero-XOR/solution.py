from collections import defaultdict as dd

N = int(input())
arr = list(map(int, input().split()))
mid = (N + 1) // 2
part_one = arr[:mid]
part_two = arr[mid:]

count = dd(int)

temp = [0]
for i in part_two:
    j = len(temp)
    while j > 0:
        j -= 1
        temp.append(i ^ temp[j])

for i in temp:
    count[i] += 1

ans = count[0]
temp = [0]
for i in part_one:
    j = len(temp)
    while j > 0:
        j -= 1
        temp.append(i ^ temp[j])
        ans += count[i ^ temp[j]]

print(ans-1)
