t = int(input())
while t > 0:
    n = int(input())
    array = list(map(int, input().split()))
    count = len(array)

    array.sort()
    for i in range(n - 1):
        if array[i] == array[i + 1]:
            count -= 1

    if count % 2 == 0:
        print("Q")
    else:
        print("P")
    t -= 1
