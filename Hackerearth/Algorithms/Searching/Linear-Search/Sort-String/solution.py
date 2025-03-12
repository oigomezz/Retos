def minimum_count_of_flips(str, n):
    zeros = str.count('0')
    if (zeros == 0 or zeros == n):
        return 0

    rones = n - zeros  # total ones and 1s right from index
    lones = 0  # 1s left from index
    min_flips = rones if rones < zeros else zeros
    for i in range(n):
        if str[i] == '1':
            sm = lones + n - i - rones
            if sm < min_flips:
                min_flips = sm
            lones += 1
            rones -= 1
    return (min_flips + 1) // 2


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(str(minimum_count_of_flips(s, n)))
