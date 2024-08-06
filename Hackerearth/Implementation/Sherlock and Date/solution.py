t = int(input())
for _ in range(t):
    day, month, year = map(str, input().strip().split())
    day = int(day)
    year = int(year)

    if day == 1 and month == "January":
        day = 31
        month = "December"
        year -= 1
    elif day == 1 and month == "February":
        day = 31
        month = "January"
    elif day == 1 and month == "March":
        if year % 4 == 0 and year % 100 != 0:
            day = 29
        else:
            day = 28
        month = "February"
    elif day == 1 and month == "April":
        day = 31
        month = "March"
    elif day == 1 and month == "May":
        day = 30
        month = "April"
    elif day == 1 and month == "June":
        day = 31
        month = "May"
    elif day == 1 and month == "July":
        day = 30
        month = "June"
    elif day == 1 and month == "August":
        day = 31
        month = "July"
    elif day == 1 and month == "September":
        day = 31
        month = "August"
    elif day == 1 and month == "October":
        day = 30
        month = "September"
    elif day == 1 and month == "November":
        day = 31
        month = "October"
    elif day == 1 and month == "December":
        day = 30
        month = "November"
    else:
        day -= 1

    print(day, month, year)
