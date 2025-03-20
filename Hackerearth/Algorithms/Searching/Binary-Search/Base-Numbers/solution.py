from sys import stdin
import math


def search_lower(a, b, n):
    lo = 1
    hi = 10**9
    val = n - math.log(a, b)
    ans = 0
    while hi >= lo:
        mid = (hi+lo)//2
        xlogx = mid*math.log(mid, b)
        if xlogx < val:
            ans = mid
            lo = mid+1
        else:
            hi = mid-1
    return ans


for line in stdin.readlines():
    a, n, b = list(map(int, line.split()))
    x_lower = search_lower(a, b, n-1)
    x_upper = search_lower(a, b, n)
    print(x_upper-x_lower)
