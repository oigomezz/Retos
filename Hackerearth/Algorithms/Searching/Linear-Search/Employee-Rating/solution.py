def solve(n, workload):
    result = 0
    cnt = 0
    for i in range(n):
        if workload[i] > 6:
            cnt += 1
        else:
            cnt = 0

        result = max(result, cnt)

    return result


N = int(input())
workload = list(map(int, input().split()))

out_ = solve(N, workload)
print(out_)
