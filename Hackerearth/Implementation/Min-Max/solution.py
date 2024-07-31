N = int(input())
min_val = 0
max_val = 0
count = 0
c = 0
a = list(map(int, input().split()))
for i in range(N):
    if count == 0:
        min_val = a[i]
        max_val = a[i]
    else:
        if a[i] < min_val:
            min_val = a[i]
        elif a[i] > max_val:
            max_val = a[i]
    count += 1

count = 0
for i in range(min_val, max_val + 1):
    count += 1

i = 0
while i < N and min_val <= max_val:
    if min_val == a[i]:
        c += 1
        i = 0
        min_val += 1
    else:
        i += 1

if c == count:
    print("YES")
else:
    print("NO")
