import math


def to_sec(time):
    (hr, mn, sec) = time.split(":")
    seconds = int(hr) * 60 * 60 + int(mn) * 60 + int(sec)
    return seconds


def overlap(time1, time2):
    start = max(time1[0], time2[0])
    end = min(time1[1], time2[1])
    return max(0, end - start)


cases = int(input())
(start, end) = map(to_sec, input().split(" "))
attendance = {start: 0,  end: 0}
for case in range(cases):
    data = input().split(" ")
    intervals = data[2:]
    if data[0] == "1":
        myintervals = intervals
    start = True
    for i in intervals:
        time = to_sec(i)
        if time not in attendance:
            attendance[time] = 0
        if start:
            attendance[time] += 1
        else:
            attendance[time] -= 1
        start = not start

events = sorted(attendance.items())
attendanceIntervals = {}
current = 0
for i in range(len(events) - 1):
    current += events[i][1]
    if current not in attendanceIntervals:
        attendanceIntervals[current] = []
    attendanceIntervals[current].append((events[i][0], events[i+1][0]))

minAtt = min(attendanceIntervals.items())[1]
totalSec = 0
overlapSec = 0
myIntervals = []
for i in range(int(len(myintervals)/2)):
    myIntervals.append((to_sec(myintervals[i*2]), to_sec(myintervals[i*2+1])))
for minInterval in minAtt:
    for i in myIntervals:
        overlapSec += overlap(minInterval, i)
    totalSec += minInterval[1] - minInterval[0]

gcd = math.gcd(overlapSec, totalSec)
if overlapSec == 0:
    print(0)
else:
    print(str(overlapSec//gcd) + "/" + str(totalSec // gcd))
