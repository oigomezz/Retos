def longest_increasing_subsequence(size, arr):
    subsequence = []
    subsequence.append(arr[0])
    for index in range(1, size):
        if arr[index] > subsequence[-1]:
            subsequence.append(arr[index])
        else:
            insert_index = next(i for i, x in enumerate(
                subsequence) if x >= arr[index])
            subsequence[insert_index] = arr[index]
    return len(subsequence)


if __name__ == "__main__":
    length = int(input())
    array = list(map(int, input().split()))
    reversed_array = array[::-1]

    answer1 = length - longest_increasing_subsequence(length, array)
    answer2 = length - longest_increasing_subsequence(length, reversed_array)

    print(min(answer1, answer2))
