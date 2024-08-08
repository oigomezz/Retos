import math

days = [0] * (7 + 10)

number_of_days = 7
total_visitors = 0
average_visitors = 0
variance = 0
standard_deviation = 0

for i in range(number_of_days):
    visitor_data = input()
    daily_visitors = 0

    for j in range(len(visitor_data)):
        if visitor_data[j] == '1':
            days[i] += 1
    total_visitors += days[i]

average_visitors = total_visitors / 7.0

for i in range(number_of_days):
    variance += (average_visitors - days[i]) ** 2

standard_deviation = math.sqrt(variance / 7.0)
print(f"{standard_deviation:.4f}")
