MOD = 1000000007
tests = int(input())
for _ in range(tests):
    gN, gK = map(int, input().split())
    gS = input()
    gDP = [[0] * 21 for _ in range(100001)]
    for i in range(gN + 1):
        gDP[i][0] = 1
    for i in range(1, gN + 1):
        gDP[i][0] = 1
        gDP[i][1] = (gDP[i - 1][1] + gDP[i - 1][0] *
                     (ord(gS[i - 1]) - ord('a'))) % MOD
        for j in range(2, gK + 1):
            gDP[i][j] = (gDP[i - 1][j] + gDP[i - 1][j - 1] * 25) % MOD
    print(gDP[gN][gK])
