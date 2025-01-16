def queue_and_stack(arr):
    ln = max(arr)
    primes = [True] * (ln + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i < ln:
        if primes[i]:
            for j in range(i * 2, ln + 1, i):
                primes[j] = False
        i += 1
    stack = []
    queue = []
    for i in arr:
        if primes[i]:
            queue.append(i)
        else:
            stack.append(i)
    return [queue, reversed(stack)]


n = int(input())
arr = list(map(int, input().strip().split()))

out_ = queue_and_stack(arr)
for i_out_ in out_:
    print(' '.join(map(str, i_out_)))
