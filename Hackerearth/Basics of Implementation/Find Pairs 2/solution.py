n, l, r = map(int, input().split())
arr = [int(x) for x in input().split()]
m = dict.fromkeys(arr, 0)

for i in range(n):
    m[arr[i]] += 1

xor_arr = 0

for key, value in m.items():
    if (value & 1):
        xor_arr ^= key

print(xor_arr)
