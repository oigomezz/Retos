def solve(arr):
    size = len(arr)
    queue = {}
    for i in arr:
        queue[i] = True
        placed = []
        if i == size:
            placed.append(i)
            size -= 1
            while size in queue:
                placed.append(size)
                size -= 1
        yield placed


N = int(input())
arr = list(map(int, input().split()))
out_ = solve(arr)

for i_out_ in out_:
    print(' '.join(map(str, i_out_)))
