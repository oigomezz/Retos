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


n = int(input())
numbers = []
for _ in range(n):
    numbers.append(input())

out_ = solve(numbers)
print(out_)
print(last_move)
