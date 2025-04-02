from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    packets = [int(input()) for _ in range(n)]
    most_common_packet = max(Counter(packets).values())
    print(most_common_packet)