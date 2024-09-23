N, M, Q = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(input())

curr_h, curr_v = 0, 0
left, right, above, down = 0, 0, 0, 0
total = 1
changed = True

for _ in range(Q):
    q = input().split()

    if q[0] == "1":
        x, y = int(q[1]), int(q[2])

        curr_h += x
        curr_v += y

        if curr_h > left:
            left = curr_h
            changed = True
        elif curr_h < right:
            right = curr_h
            changed = True

        if curr_v > above:
            above = curr_v
            changed = True
        elif curr_v < down:
            down = curr_v
            changed = True
    else:
        if total == 0 or left + abs(right) >= M or abs(down) + above >= N:
            print(0)
            continue

        if not changed:
            print(total)
            continue

        total = 0
        for row in range(above, N - abs(down)):
            for col in range(left, M - abs(right)):
                if grid[row][col] == "1":
                    total += 1

        print(total)
        changed = False
