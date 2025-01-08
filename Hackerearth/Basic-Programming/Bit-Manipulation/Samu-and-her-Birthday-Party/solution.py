from functools import cmp_to_key


def bitcompare(x, y):
    return bin(x).count('1') - bin(y).count('1')


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = []
        for i in range(n):
            str_num = input()
            arr.append(int(str_num, 2))

        arr.sort(key=cmp_to_key(bitcompare))
        res = 11

        for i in range(1, 1 << k):
            mask = i
            for a in arr:
                if not (mask & a):
                    mask = 0
                    break
            if mask:
                res = min(res, bin(mask).count('1'))

        print(res)


if __name__ == "__main__":
    main()
