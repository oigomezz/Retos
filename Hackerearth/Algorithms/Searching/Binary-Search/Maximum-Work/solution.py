def solve(magical_pills, strength, workers, strength_workers, tasks, strength_required):
    strength_required.sort()
    strength_workers.sort()
    s, e, val = 1, min(workers, tasks), 0
    while s <= e:
        mid = (s + e) // 2
        req = 0
        for i in range(mid):
            req += (max(0, strength_required[i] - strength_workers[workers - (
                mid - i)]) + strength - 1) // strength
        if req <= magical_pills:
            val = mid
            s = mid + 1
        else:
            e = mid - 1
    return val


T = int(input())
for _ in range(T):
    K, B = map(int, input().split())
    N = int(input())
    W = list(map(int, input().split()))
    M = int(input())
    S = list(map(int, input().split()))

    out_ = solve(K, B, N, W, M, S)
    print(out_)
