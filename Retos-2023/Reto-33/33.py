def thirty_leap_years(year):
    current_year = year + 1
    year_count = 0

    while year_count < 30:
        if current_year % 4 == 0 and (
            current_year % 100 != 0 or current_year % 400 == 0
        ):
            print(current_year)
            year_count += 1

        current_year += 1


thirty_leap_years(1999)
thirty_leap_years(-500)
