def mod(a: int) -> int:
    if a < 0:
        return -a
    return a


test_cases = int(input())
for _ in range(test_cases):
    n, a, b, c, d, move = map(int, input().split())
    if move == 0:
        if c >= a and mod(d - b) <= (n - a):
            print("Draw")
        else:
            print("White Wins")
    else:
        if c >= a - 1 and mod(d - b) <= (n - a + 1):
            print("Draw")
        else:
            print("White Wins")
