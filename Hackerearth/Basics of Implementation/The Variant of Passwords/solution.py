T = int(input())

for i in range(T):
    N, A, B = map(int, input().split())
    s = input()
    twos = N - (A + B)
    ans = ""
    rep = 0
    has = [0, 0, 0]
    req = [0, 0, 0]
    char_array = list(s)

    # Storing how many 0's, 1's and 2's are present in string
    for char in char_array:
        index = int(char)
        has[index] += 1

    # To check if there is a requirement of a character
    req[0] = A - has[0]
    req[1] = B - has[1]
    req[2] = twos - has[2]

    i = 0
    j = N - 1

    while j >= 0:
        # BACKWARDS
        jth = char_array[j]

        # Checking if any extra 0's should be replaced by 2's or 1's
        if jth == '0' and req[0] < 0:
            if req[2] > 0:
                char_array[j] = '2'
                req[2] -= 1
            elif req[1] > 0:
                char_array[j] = '1'
                req[1] -= 1
            req[0] += 1
            rep += 1

        # Checking if any extra 1's should be replaced by 2's
        elif jth == '1' and req[1] < 0 and req[2] > 0:
            char_array[j] = '2'
            req[2] -= 1
            req[1] += 1
            rep += 1

        # FORWARDS
        ith = char_array[i]

        # Checking if any extra 2's should be replaced by 0's or 1's
        if ith == '2' and req[2] < 0:
            if req[0] > 0:
                char_array[i] = '0'
                req[0] -= 1
            elif req[1] > 0:
                char_array[i] = '1'
                req[1] -= 1
            req[2] += 1
            rep += 1

        # Checking if any extra 1's should be replaced by 0's
        elif ith == '1' and req[1] < 0 and req[0] > 0:
            char_array[i] = '0'
            req[0] -= 1
            req[1] += 1
            rep += 1

        i += 1
        j -= 1

    ans = "".join(char_array)
    print(rep)
    print(ans)
