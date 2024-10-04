from collections import defaultdict
from operator import itemgetter
from string import ascii_lowercase
from itertools import chain

t = int(input())
for _ in range(t):
    s = input().strip()
    counter = defaultdict(list)
    for c in reversed(ascii_lowercase):
        times = s.count(c)
        counter[times].append(c)
        if len(counter[times]) > 1:
            counter[times].sort(reverse=True)
    ans = [item[-1] for item in sorted(counter.items(), key=itemgetter(0))]
    print(' '.join(chain.from_iterable(ans)))
