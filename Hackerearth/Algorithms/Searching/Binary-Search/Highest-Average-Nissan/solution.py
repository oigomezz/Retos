def bin_search(avg_arr: list[tuple], x: int):
    lo, hi = 0, len(avg_arr)-1
    res = -1

    while lo <= hi:
        md = lo + (hi-lo)//2
        ele, _ = avg_arr[md]

        if ele >= x:
            hi = md-1
        else:
            res = md
            lo = md+1

    return res


def average_less_than_k(arr: list[int], queries: list[int]):
    arr.sort()
    avg_arr = []

    csm = 0
    cnt = 0
    for ind, i in enumerate(arr):
        csm += i
        cnt += 1
        avg_arr.append((csm/cnt, ind))

    avg_arr.sort()
    mx_avg = []
    mx = 0
    for _, j in avg_arr:
        mx = max(mx, j)
        mx_avg.append(mx)

    for i in queries:
        ind = bin_search(avg_arr, i)
        if ind == -1:
            print("0")
        else:
            print(mx_avg[ind] + 1)


N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
queries = [int(input()) for _ in range(Q)]
average_less_than_k(arr, queries)
