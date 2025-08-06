from functools import lru_cache


@lru_cache(maxsize=None)
def Min_and_Max(arr):
    if len(arr) == 2:
        power = arr[0] ^ arr[1]
        return power, power
    minimum = float('inf')
    maximum = 0
    for i in range(1, len(arr)):
        val = arr[0] ^ arr[i]
        res = Min_and_Max(arr[1:i] + arr[i + 1:])
        minimum = min(res[0] + val, minimum)
        maximum = max(res[1] + val, maximum)
    return minimum, maximum


n = int(input())
Arr = []
for _ in range(n):
    Arr.append(int(input()))

out_ = Min_and_Max(tuple(Arr))
print(' '.join(map(str, out_)))
