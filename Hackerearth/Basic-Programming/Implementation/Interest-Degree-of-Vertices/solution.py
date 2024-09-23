n = int(input())
sum_val = 0
childs = [0] * n
make_zero = False

arr = list(map(int, input().split()))
for i in range(n - 1):
    parent = arr[i]
    childs[parent] += 1
    if childs[parent] >= 2:
        make_zero = True

arr2 = list(map(int, input().split()))
for i in range(n):
    x = arr2[i]
    sum_val += x

if make_zero:
    print(sum_val)
else:
    print(0)
