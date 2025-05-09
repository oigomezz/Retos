from heapq import heapify, heappop, heappush

n, q = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
answers = {0: sum(arr)}
small_heap = arr.copy()
large_heap = [-i for i in arr]
heapify(small_heap)
heapify(large_heap)
for i in range(1, n):
    smallest = heappop(small_heap)
    largest = -heappop(large_heap)
    heappush(small_heap, largest - smallest)
    heappush(large_heap, smallest - largest)
    answers[i] = answers[i - 1] - 2 * smallest

for _ in range(q):
    k = int(input())
    print(answers[k])
