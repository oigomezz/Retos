test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    d = dict()
    arr = [int(num) for num in input().split()]
    for item in arr:
        try:
            d[item] += 1
        except KeyError:
            d[item] = 1
    dik = sorted(d.items())
    print('Lucky' if dik[0][1] & 1 else 'Unlucky')
