n, m = map(int, input().split())
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))
x, y = map(int, input().split())

arr = []

for i in range(n):
    for j in range(m):
        arr.append([arr1[i]+arr2[j], i+1, j+1])
arr = sorted(arr)
arr = arr[x:y-1]
print(len(arr))
for i in range(len(arr)):
    print("(", arr[i][1], ",", arr[i][2], ")", sep="", end=" ")
print()
