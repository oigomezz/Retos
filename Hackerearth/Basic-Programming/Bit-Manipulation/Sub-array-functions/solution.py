import heapq

t = int(input())
results = []
for _ in range(t):
    n, m, p = map(int, input().split())
    array_a = list(map(int, input().split()))

    left_index = -1
    right_index = -1
    result = 0

    for i in range(n):
        max_heap = []
        min_heap = []
        heapq.heappush(max_heap, -array_a[i])
        heapq.heappush(min_heap, array_a[i])

        limit = min(p, m) - 1
        if limit + i > n:
            break

        func1 = array_a[i]
        func2 = array_a[i]
        max_func3 = float('-inf')
        max_j = -1

        for j in range(i + 1, n):
            if len(max_heap) < m:
                heapq.heappush(max_heap, -array_a[j])
                func1 ^= array_a[j]
            elif -max_heap[0] > array_a[j]:
                func1 ^= -max_heap[0]
                func1 ^= array_a[j]
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -array_a[j])

            if len(min_heap) < p:
                heapq.heappush(min_heap, array_a[j])
                func2 ^= array_a[j]
            elif min_heap[0] < array_a[j]:
                func2 ^= min_heap[0]
                func2 ^= array_a[j]
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, array_a[j])

            if len(min_heap) == p and len(max_heap) == m:
                func3 = func1 & func2
                if max_func3 <= func3:
                    max_func3 = func3
                    max_j = j

        if result < max_func3 or (result == max_func3 and (right_index - left_index) < (max_j - i)):
            left_index = i + 1
            right_index = max_j + 1
            result = max_func3

    results.append(f"{left_index} {right_index} {result}")

print("\n".join(results))
