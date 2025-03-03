import math

levels, s = map(int, input().split())
assert 1 <= levels <= 30
assert 1 <= s <= 1000000000000000000

q = int(input())

pow = [1] * 100
pro = 1
for i in range(1, levels):
    pro *= 2
    pow[i] = pro

if levels > 1:
    x = (s - ((pro - 1) * (pro - 1))) // (pro * 2 - 1) + 1
else:
    x = s + 1

root = 0 if levels < 2 else pow[levels - 2] - 1

for _ in range(q):
    line = list(map(int, input().split()))
    type_query = line[0]

    if type_query == 0:
        val = line[1]
        cnt = levels - 3
        val -= x

        if levels > 1 and val == pow[levels - 1] - 1:
            print("r" * (levels - 1))
        else:
            temp = root
            if val == temp:
                print("root")
            else:
                while temp != val:
                    if temp > val:
                        print("l", end="")
                        temp -= pow[cnt]
                    else:
                        print("r", end="")
                        temp += pow[cnt]
                    cnt -= 1
                print()
    else:
        k = line[1]
        l = math.floor(math.log2(k)) + 1
        if l == levels:
            a = x
        else:
            a = x + pow[levels - l - 1] - 1

        n = k - pow[l - 1] + 1
        d = pow[levels - l]
        print(a + (n - 1) * d)
