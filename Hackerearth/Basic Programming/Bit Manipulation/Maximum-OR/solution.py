test_cases = int(input())
for _ in range(test_cases):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))

    answer = 0
    for i in range(61, -1, -1):
        minimum = float('inf')
        id = -1
        for j in range(n):
            if (array[j] >> i) & 1:
                minimum = 0
                id = j
            elif minimum >= (1 << i) - (array[j] & (1 << i) - 1):
                minimum = (1 << i) - (array[j] & (1 << i) - 1)
                id = j

        if minimum <= k:
            k -= minimum
            array[id] += minimum
            answer |= 1 << i

    print(answer)
