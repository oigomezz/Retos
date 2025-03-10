if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        n, m = map(int, input().split())
        v = list(map(int, input().split()))
        res = -1
        m -= 1

        for i in range(29, -1, -1):
            temp = m >> i
            if (temp & 1) == 0:
                temp |= 1
                may = 0
                for x in v:
                    if (temp & (x >> i)) == temp:
                        may += 1
                if may:
                    res = max(res, may)

        print(res)
