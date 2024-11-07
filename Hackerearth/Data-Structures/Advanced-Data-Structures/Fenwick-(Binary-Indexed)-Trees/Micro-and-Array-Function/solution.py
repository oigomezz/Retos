def read(bit, idx):
    total_sum = 0
    if idx == 0:
        return 0
    while idx > 0:
        total_sum += bit[idx]
        idx -= (idx & -idx)
    return total_sum


def update(bit, idx, value):
    while idx <= 200000:
        bit[idx] += value
        idx += (idx & -idx)


def calc(arr, num_count, offset_map):
    result = 0
    tree = [0] * 200005
    for i in range(1, num_count + 1):
        result += read(tree, offset_map[arr[i] - K]) * (num_count - i + 1)
        update(tree, offset_map[arr[i]], i)
    return result


if __name__ == "__main__":
    T = int(input())
    results = []

    while T > 0:
        T -= 1
        N, K = map(int, input().split())
        arr = [0] * (N + 1)
        value_list = []
        line = list(map(int, input().split()))

        for i in range(1, N + 1):
            arr[i] = int(line[i-1])
            value_list.append(arr[i])
            value_list.append(arr[i] - K)

        value_list = sorted(set(value_list))
        offset_map = {value: i + 1 for i, value in enumerate(value_list)}

        answer = calc(arr, N, offset_map)
        arr[1:N + 1] = reversed(arr[1:N + 1])
        answer += calc(arr, N, offset_map)

        results.append(str(answer))

    print("\n".join(results))
