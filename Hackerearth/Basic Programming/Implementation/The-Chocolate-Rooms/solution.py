T = int(input())

for case in range(T):
    n, k = map(int, input().split())
    chocolates = set()

    for room in range(n):
        [chocolates.add(x) for x in input().split() if x.isalpha()]

    print('Yes' if len(chocolates) == k else 'No')
