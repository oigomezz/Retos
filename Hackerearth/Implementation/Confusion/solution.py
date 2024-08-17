n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = int(input())
    distinct = set()
    for i in range(query, n+1):
        distinct.add(arr[i-1])
    print(len(distinct))
