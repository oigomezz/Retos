def calculate_mex(arr):
    seen = set()
    current_mex = 0
    result = []

    for num in arr:
        seen.add(num)
        while current_mex in seen:
            current_mex += 1
        result.append(current_mex)

    return result


n = int(input())
arr = list(map(int, input().split()))
result = calculate_mex(arr)
print(" ".join(map(str, result)))
