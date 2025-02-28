from functools import reduce


n, q = map(int, input().split())
array = [0] * 1000017
for _ in range(q):
    line = list(map(int, input().split()))
    type = int(line[0])
    left = int(line[1]) - 1
    right = int(line[2])

    if type < 4:
        value = int(line[3])
        while left < right:
            if type == 1:
                array[left] |= value
            elif type == 2:
                array[left] &= value
            else:
                array[left] ^= value
            left += 1
    elif type == 4:
        print(sum(array[left:right]))
    else:
        print(reduce(lambda a, b: a ^ b, array[left:right]))
