n, k = map(int, input().split())
arr = list(map(int, input().split()))
mp = {x: i+1 for i, x in enumerate(arr)}
arr.sort(reverse=True)

for i in range(k):
    print(mp[arr[i]], end=" ")