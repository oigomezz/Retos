T = int(input())
results = []

for _ in range(T):
    n = int(input())
    pos = [0] * 31
    ans = 0
    arr = list(map(int, input().split()))

    for i in range(1, n + 1):
        a = arr[i-1]
        temp = [0]

        for j in range(31):
            if a & (1 << j):
                pos[j] = i
            temp.append(pos[j])

        temp.sort()
        pos_index = 31
        num = 0

        while True:
            num += 1
            while pos_index > 0 and temp[pos_index - 1] == temp[pos_index]:
                pos_index -= 1
                num += 1

            if num % 2:
                ans += (temp[pos_index] - temp[pos_index - 1])

            if pos_index == 0:
                break

            pos_index -= 1

    results.append(str(ans))

print("\n".join(results))
