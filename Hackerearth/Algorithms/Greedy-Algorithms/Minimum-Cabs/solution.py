from collections import defaultdict
from itertools import accumulate

n = int(input())
timer = defaultdict(int)
for _ in range(n):
    hh1, mm1, hh2, mm2 = map(int, input().strip().split())
    start_time = hh1 * 60 + mm1  # minutes
    end_time = hh2 * 60 + mm2  # minutes
    timer[start_time] += 1
    timer[end_time + 1] -= 1

print(max(accumulate(car for _, car in sorted(timer.items()))))
