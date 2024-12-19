from math import gcd


class Jef:
    def __init__(self, times, inp):
        self.times = times
        self.inp = inp


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        a = 0
        b = 0
        count = 0

        for _ in range(n):
            times, inp = input().split()
            times = int(times)
            arr.append(Jef(times, inp))
            if inp == 'A':
                a += times
            else:
                b += times

        if a == 0 or b == 0:
            print(max(a, b))
            continue

        gc = gcd(a, b)
        a //= gc
        b //= gc
        ratio_a = 0
        ratio_b = 0

        for jef in arr:
            if jef.inp == 'A':
                ratio_a += jef.times
                if ratio_b != 0 and ratio_b % b == 0:
                    qu = ratio_b // b
                    if ratio_a >= qu * a and (ratio_a - jef.times) < qu * a:
                        count += 1
                        ratio_b = 0
                        ratio_a -= qu * a
            else:
                ratio_b += jef.times
                if ratio_a != 0 and ratio_a % a == 0:
                    qu = ratio_a // a
                    if ratio_b >= qu * b and (ratio_b - jef.times) < qu * b:
                        count += 1
                        ratio_a = 0
                        ratio_b -= qu * b

        print(count)


if __name__ == "__main__":
    main()
