t = int(input())
for _ in range(t):
    n = int(input())
    arrival_times = list(map(int, input().strip().split()))
    durations = list(map(int, input().strip().split()))
    longest = max(sum(z) for z in zip(arrival_times, durations))
    calc = [0] * longest
    for z in zip(arrival_times, durations):
        calc[z[0] - 1] += 1
        calc[z[0] + z[1] - 1] -= 1
    total = 0
    rooms = 0
    for i in calc:
        total += i
        rooms = max(rooms, total)

    print(rooms)
