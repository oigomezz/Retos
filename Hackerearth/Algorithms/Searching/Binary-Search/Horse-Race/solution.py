import heapq

for case in range(int(input())):
    n, m, x = map(int, input().split())
    race_winner = list(map(int, input().split()))
    horse_win_fre = [0]*(m+1)
    not_mon_fre = 0
    for horse in race_winner:
        if horse > m:
            not_mon_fre += 1
            continue
        horse_win_fre[horse] += 1
    heap = [fre for fre in horse_win_fre[1:m+1]]
    heapq.heapify(heap)
    while x and not_mon_fre:
        heapq.heapreplace(heap, heap[0]+1)
        x -= 1
        not_mon_fre -= 1

    li = []
    while heap:
        li.append(heapq.heappop(heap))

    low, high = li[0], li[-1] + 1
    while low < high:
        mid = (low + high + 1)//2
        lx, hx = 0, 0
        for el in li:
            if el < mid:
                lx += mid - el
            elif mid < el:
                hx += el - mid
        if lx <= x and lx <= hx:
            low = mid
        else:
            high = mid-1

    print(low)
