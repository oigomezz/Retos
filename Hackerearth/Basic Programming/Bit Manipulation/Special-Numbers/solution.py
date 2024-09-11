t = int(input())
results = []
for _ in range(t):
    k = int(input())
    assert k <= int(1e9)

    length = 1
    curr = 0
    next_val = 4

    while curr + next_val < k:
        curr += next_val
        next_val *= 4
        length += 1

    k -= curr
    k -= 1
    temp = []
    tmp = length

    while tmp > 0:
        to = k % 4
        k //= 4
        temp.append(chr(to + ord('a')))
        tmp -= 1

    put = ''.join(temp)
    temp.reverse()
    results.append(''.join(temp) + put)

print('\n'.join(results))
