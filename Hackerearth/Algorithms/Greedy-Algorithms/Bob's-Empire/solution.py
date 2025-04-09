test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    abcd = list(map(int, input().strip().split()))
    print(max((n + i - 1) // i for i in abcd) + 3)