prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

n = int(input())
a = list(map(int, input().split()))
frequency_map = {}
arr = [0] * 25
frequency_map[tuple(arr)] = frequency_map.get(tuple(arr), 0) + 1
result = 0

for i in range(n):
    for j in range(25):
        while a[i] % prime_numbers[j] == 0:
            arr[j] += 1
            arr[j] %= 3
            a[i] //= prime_numbers[j]
    result += frequency_map.get(tuple(arr), 0)
    frequency_map[tuple(arr)] = frequency_map.get(tuple(arr), 0) + 1

print(result)
