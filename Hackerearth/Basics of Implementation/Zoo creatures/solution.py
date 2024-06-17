def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b//gcd(a, b)


def main():
    t = int(input())
    for _ in range(t):
        inp = input()
        input1 = inp.split()
        a = float(input1[0])
        b = float(input1[1])
        result = lcm(a, b)
        print(int(round(result/a, 0)), int(round(result/b, 0)))


if __name__ == '__main__':
    main()
