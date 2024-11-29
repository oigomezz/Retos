import datetime
import re


def print_days_between(first_date, second_date):
    try:
        print(days_between(first_date, second_date))
    except DaysBetweenError:
        print("Error en el formato de alguna fecha")
    except Exception:
        print("Error en el parse de alguna fecha")


class DaysBetweenError(Exception):
    pass


def days_between(first_date, second_date):
    formatter = datetime.datetime.strptime
    first_parsed_date = formatter(first_date, "%d/%m/%Y")
    second_parsed_date = formatter(second_date, "%d/%m/%Y")

    regex = "^([0-9]){2}[/]([0-9]){2}[/]([0-9]){4}$"

    if (
        first_parsed_date is not None
        and second_parsed_date is not None
        and re.match(regex, first_date)
        and re.match(regex, second_date)
    ):

        return abs((first_parsed_date - second_parsed_date).days)

    raise DaysBetweenError()


print_days_between("18/05/2022", "29/05/2022")
print_days_between("mouredev", "29/04/2022")
print_days_between("18/5/2022", "29/04/2022")
