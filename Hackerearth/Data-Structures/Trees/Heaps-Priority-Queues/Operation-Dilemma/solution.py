import heapq

t = int(input())
for _ in range(t):
    N, L, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pqA = []
    pqB = []
    sumA = 0
    sumB1 = 0
    sumB2 = 0
    res = 0
    inPQA = [False] * N
    inPQB = [False] * N
    l = 0

    for r in range(N):
        sumA += a[r]
        heapq.heappush(pqB, (b[r], r))
        sumB2 += b[r]
        inPQB[r] = True

        if l < r - L + 1:
            sumA -= a[l]
            if inPQA[l]:
                sumB1 -= b[l]
            else:
                sumB2 -= b[l]
            l += 1

        while len(pqA) < K and pqB and b[pqB[0][1]] > 0:
            i = heapq.heappop(pqB)[1]
            heapq.heappush(pqA, (-b[i], i))
            inPQA[i] = True
            inPQB[i] = False
            sumB1 += b[i]
            sumB2 -= b[i]

        while pqA and pqA[0][1] < l:
            heapq.heappop(pqA)
        while pqB and pqB[0][1] < l:
            heapq.heappop(pqB)

        while pqA and pqB and b[pqA[0][1]] < b[pqB[0][1]]:
            aToB = pqA[0][1]
            bToA = pqB[0][1]
            heapq.heappop(pqA)
            heapq.heappop(pqB)
            sumB1 -= b[aToB]
            sumB2 += b[aToB]
            sumB1 += b[bToA]
            sumB2 -= b[bToA]
            inPQA[aToB] = inPQB[bToA] = False
            inPQB[aToB] = inPQA[bToA] = True
            heapq.heappush(pqA, (-b[bToA], bToA))
            heapq.heappush(pqB, (b[aToB], aToB))

            while pqA and pqA[0][1] < l:
                heapq.heappop(pqA)
            while pqB and pqB[0][1] < l:
                heapq.heappop(pqB)

        if r - l + 1 == L:
            res = max(res, sumA + sumB1 - sumB2)

    print(res)
