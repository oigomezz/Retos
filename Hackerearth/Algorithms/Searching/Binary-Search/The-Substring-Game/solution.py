s = input()
q = int(input())
qry = list(map(int, input().split()))
n = len(s)
tot = n*(n+1)//2
arr = [0]
m = n
for i in range(m):
    arr.append(arr[-1]+n)
    n -= 1
for num in qry:
    if num > tot:
        print(-1)
    else:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo+hi) >> 1
            if num > arr[mid]:
                lo = mid+1
            else:
                hi = mid
        lo -= 1
        print(s[lo:lo+num-arr[lo]])
