def solve(m, n, p, matrix):
    count = 0
    for left in range(n):
        temp = [0] * m
        for right in range(left, n):
            for i in range(m):
                temp[i] += matrix[i][right]
            count += count_subarray(temp, m, p)
    return count

def count_subarray(temp, m, p):
    c_sum = [0] * p
    sum_val = 0
    result = 0
    for i in range(m):
        sum_val += temp[i]
        c_sum[(sum_val % p + p) % p] += 1
    for j in range(p):
        if c_sum[j] > 1:
            result += (c_sum[j] * (c_sum[j] - 1)) // 2
    result += c_sum[0]
    return result


M, N, P = map(int, input().split())
Matrix = []

for _ in range(M):
    Matrix.append(list(map(int, input().split())))

out_ = solve(M, N, P, Matrix)
print(out_)
