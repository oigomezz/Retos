def modified_counting_sort(arr):
    count_arr = {}
    for element in arr:
        if element in count_arr:
            count_arr[element] += 1
        else:
            count_arr[element] = 1

    ans = 0
    for index in count_arr:
        count = count_arr[index]
        ans += ((count)*(count+1))//2
    return ans


n = int(input())
for _ in range(n):
    size = int(input())
    arr = list(map(int, input().split()))
    print(modified_counting_sort(arr))
