import math

T = int(input())
for _ in range(T):
    S = int(input())

    # let 1 square of 1 width
    max_width = math.floor(math.sqrt(S))
    num_rect = 0

    # here i is width of rect
    for i in range(1, max_width + 1):
        # (S//i) represents number of rect can be formed of i width.
        # (i - 1) represents number of rect already added of i width in previous loop.
        num_rect += (S//i) - (i - 1)

    print(num_rect)
