def find_win_arr(arr, weight, n):
    i = j = 0
    cnt = 0
    while (i < n):
        j = i
        curr_sum = 0
        while (j < n):
            curr_sum += arr[j]

            if curr_sum == weight:
                cnt += 1
            elif curr_sum > weight:
                break
            j += 1
        i += 1
    return cnt


weight = {}
weight['a'] = 1
weight['b'] = 2
weight['c'] = 3
weight['d'] = 4
weight['e'] = 5
weight['f'] = 6
weight['g'] = 7
weight['h'] = 8
weight['i'] = 9
weight['j'] = 10
weight['k'] = 11
weight['l'] = 12
weight['m'] = 13
weight['n'] = 14
weight['o'] = 15
weight['p'] = 16
weight['q'] = 17
weight['r'] = 18
weight['s'] = 19
weight['t'] = 20
weight['u'] = 21
weight['v'] = 22
weight['w'] = 23
weight['x'] = 24
weight['y'] = 25
weight['z'] = 26

T = int(input())
for _ in range(T):
    k = int(input())
    arr = [weight[c] for c in list(input())]

    n = len(arr)
    print(find_win_arr(arr, k, n))
