T = int(input())
while T > 0:
    M = int(input())
    total_sum = 0
    for _ in range(M):
        len_i, d_i = map(int, input().split())
        total_sum += len_i * d_i
        while total_sum > 9:
            total_sum = sum(int(digit) for digit in str(total_sum))
    print(total_sum)
    T -= 1
