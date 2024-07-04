def main():
    b, k = map(int, input().split())
    if not b or not k or k == 9:
        print(-1)
    else:
        start_len, end_len = 0, 0
        for j in range(k):
            start_len = start_len*10 + (j+1)
            end_len = end_len*10 + (9-j)

        for num in range(start_len, end_len+1):
            num_str = str(num).replace('0', '1')
            num = int(num_str)
            num_str = str(num)
            if len(set(num_str)) == len(num_str) and dig_sum(num) == b:
                print(num)
                break
            num += 1


def dig_sum(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9


if __name__ == '__main__':
    main()
