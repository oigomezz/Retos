def find_highest_rating(q, arr, m):
    size = max(arr) + 1
    freq = [0] * size
    for i in arr:
        freq[i] += 1
    highest = 0
    for i in range(size):
        cnt = freq[i]
        for j in range(1, q + 1):
            left = i - j * m
            right = i + j * m
            if left >= 0:
                cnt += freq[left]
            if right < size:
                cnt += freq[right]
        highest = max(highest, cnt)
    return highest


M = int(input())
Q = int(input())
N = int(input())
arr = list(map(int, input().strip().split()))

out_ = find_highest_rating(Q, arr, M)
print(out_)