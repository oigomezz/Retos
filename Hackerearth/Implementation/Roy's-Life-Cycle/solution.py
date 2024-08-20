number_of_days = int(input())
max_all = max_per_day = max_count = count = 0
work = []

for day in range(number_of_days):
    ch = list(input())
    work.append(ch)

for day in range(number_of_days):
    for char_index in range(len(ch)):
        if work[day][char_index] == 'C':
            count += 1
            max_count += 1
        else:
            if count > max_per_day:
                max_per_day = count
            if max_count > max_all:
                max_all = max_count
            max_count = 0
            count = 0
    if count > max_per_day:
        max_per_day = count
    if max_count > max_all:
        max_all = max_count
    count = 0

print(max_per_day, max_all)
