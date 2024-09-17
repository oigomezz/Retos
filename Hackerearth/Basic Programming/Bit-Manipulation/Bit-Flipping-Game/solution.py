last_move = 0


def solve(number):
    global last_move
    flips = set()
    for num in number:
        for i in range(len(num)):
            if num[i] == "1":
                flips.add(i)
    last_move = len(flips)
    if last_move % 2:
        return "A"
    return "B"


N = int(input())
Number = []
for _ in range(N):
    Number.append(input())

out_ = solve(Number)
print(out_)
print(last_move)
