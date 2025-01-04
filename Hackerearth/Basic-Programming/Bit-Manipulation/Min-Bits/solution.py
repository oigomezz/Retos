test_cases = int(input())
results = []

for _ in range(test_cases):
    left, right = map(int, input().split())
    answer = 0

    while True:
        if left == 1:
            answer += 1
            break
        bits = 64 - (left - 1).bit_length()
        threshold = 1 << bits

        if threshold <= right:
            answer += threshold
            break

        threshold //= 2
        answer += threshold
        left -= threshold
        right -= threshold

    results.append(answer)

print("\n".join(map(str, results)))
