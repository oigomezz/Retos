def sum_of_digit(num):
    sum_dig = 0
    while (num > 0):
        sum_dig = sum_dig + num % 10
        num = num//10
    return sum_dig


arr = [0]
for i in range(1, 136):
    sum_dig = i*i*i
    new_arr = [sum_dig]
    while (True):
        temp = sum_dig
        sum_dig = 0
        sum_dig = sum_of_digit(temp)
        sum_dig = sum_dig*sum_dig*sum_dig
        if (sum_dig not in new_arr):
            new_arr.append(sum_dig)
        else:
            break
    arr.append(new_arr)

testc = int(input())
for _ in range(testc):
    n, k = map(int, input().split())
    sum_dig = sum_of_digit(n)
    if (k == 1):
        print(arr[sum_dig][0])
    elif (k == 2):
        if (len(arr[sum_dig]) == 1):
            print(arr[sum_dig][0])
        else:
            print(arr[sum_dig][1])
    else:
        if (len(arr[sum_dig]) == 1):
            print(arr[sum_dig][0])
        elif (len(arr[sum_dig]) == 2):
            if (sum_of_digit(arr[sum_dig][0]) == sum_of_digit(arr[sum_dig][1])):
                print(arr[sum_dig][1])
            else:
                if (k % 2 == 0):
                    print(arr[sum_dig][1])
                else:
                    print(arr[sum_dig][0])
        elif (len(arr[sum_dig]) == 3):
            if (sum_of_digit(arr[sum_dig][1]) == sum_of_digit(arr[sum_dig][2])):
                print(arr[sum_dig][2])
            else:
                if (k % 2 == 0):
                    print(arr[sum_dig][1])
                else:
                    print(arr[sum_dig][2])
        else:
            if (k % 2 != 0):
                print(arr[sum_dig][2])
            else:
                print(arr[sum_dig][3])
