def time_to_millis(days, hours, minutes, seconds):
    days_in_millis = days * 24 * 60 * 60 * 1000
    hours_in_millis = hours * 60 * 60 * 1000
    minutes_in_millis = minutes * 60 * 1000
    seconds_to_millis = seconds * 1000

    return days_in_millis + hours_in_millis + minutes_in_millis + seconds_to_millis


print(time_to_millis(0, 0, 0, 10))
print(time_to_millis(2, 5, -45, 10))
print(time_to_millis(2000000000, 5, 45, 10))
