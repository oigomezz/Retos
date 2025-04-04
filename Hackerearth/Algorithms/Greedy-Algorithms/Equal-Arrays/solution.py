testcase = int(input())
for _ in range(testcase):
    N, M = map(int, input().split())
    arrayA = list(map(int, input().split()))
    arrayB = list(map(int, input().split()))
    maximumLength = -1
    if sum(arrayA) == sum(arrayB):
        currentIndexA = currentIndexB = 0
        equalA, equalB = [], []
        # Trying to equalize elements by adding on following elements to the shorter side of an array
        while currentIndexA < N and currentIndexB < M:
            if not equalA:
                equalA.append(arrayA[currentIndexA])
                currentIndexA += 1
            if not equalB:
                equalB.append(arrayB[currentIndexB])
                currentIndexB += 1
            if equalA[-1] < equalB[-1]:
                equalA[-1] += arrayA[currentIndexA]
                currentIndexA += 1
            elif equalB[-1] < equalA[-1]:
                equalB[-1] += arrayB[currentIndexB]
                currentIndexB += 1
            else:
                equalA.append(arrayA[currentIndexA])
                currentIndexA += 1
                equalB.append(arrayB[currentIndexB])
                currentIndexB += 1
        # Combining remaining elements (if any) in equal arrays
        while currentIndexA < N:
            equalA[-1] += arrayA[currentIndexA]
            currentIndexA += 1
        while currentIndexB < M:
            equalB[-1] += arrayB[currentIndexB]
            currentIndexB += 1
        if equalA == equalB:
            maximumLength = len(equalA)
    print(str(maximumLength))
