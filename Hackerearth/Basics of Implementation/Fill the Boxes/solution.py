t = int(input())
while t > 0:
    n, m, k = list(map(int, input().split()))
    capacity = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    capacity.sort()
    weights.sort()

    weights_count = 0
    capacity_count = 0
    count = 0

    while weights_count < m and capacity_count < n:
        if weights[weights_count] >= capacity[capacity_count] and weights[weights_count] <= capacity[capacity_count] + k:
            count += 1
            capacity_count += 1
            weights_count += 1
        elif weights[weights_count] < capacity[capacity_count]:
            weights_count += 1
        else:
            capacity_count += 1

    print(count)
    t -= 1
