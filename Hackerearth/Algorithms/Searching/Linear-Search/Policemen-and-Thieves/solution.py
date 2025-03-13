def solution(arr, k):
    ans = 0
    if k > len(arr):
        for row in arr:
            ans += (min(row.count("T"), row.count("P")))
        return ans

    for row in arr:
        arr_len = len(row)
        for i in range(arr_len):
            if row[i] == 'P':
                thieve_found = False
                for thief in range(max(0, i-k), min(i+k+1, arr_len)):
                    if row[thief] == 'T':
                        row[thief] = 'X'
                        thieve_found = True
                        break

                if thieve_found:
                    ans += 1
    return ans


T = input()
for _ in range(T):
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input().split())
    out_ = solution(A, K)
    print(out_)
