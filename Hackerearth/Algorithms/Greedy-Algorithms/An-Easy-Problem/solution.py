from datetime import datetime, timedelta

time = input().strip()
x = int(input())
hh, mm = map(int, time.split(':'))
dt = datetime.strptime(time, '%H:%M')
td = timedelta(minutes=1)
t_minutes = 0
while True:
    hours = dt.hour
    minutes = dt.minute
    total = sum(divmod(hours, 10)) + sum(divmod(minutes, 10))
    if total % x == 0:
        print(t_minutes)
        break
    dt += td
    if dt.hour == hh and dt.minute == mm:
        print(-1)
        break
    t_minutes += 1
