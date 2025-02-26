arr = [0] * 1000005
output = [0] * 1000005


def countsort(n, place):
    freq = [0] * 100000
    for i in range(n):
        freq[(arr[i] // place) % 100000] += 1
        output[i] = 0
    for i in range(1, 100000):
        freq[i] += freq[i - 1]
    for i in range(n - 1, -1, -1):
        output[freq[(arr[i] // place) % 100000] - 1] = arr[i]
        freq[(arr[i] // place) % 100000] -= 1
    for i in range(n):
        arr[i] = output[i]
        print(arr[i], end=" ")
    print()


n = int(input())
maxx = -1
data = list(map(int, input().split()))
for i in range(n):
    arr[i] = int(data[i])
    maxx = max(maxx, arr[i])

i = 1
while maxx // i:
    countsort(n, i)
    i *= 100000
