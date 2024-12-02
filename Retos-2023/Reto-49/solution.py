from datetime import datetime


def diff_time_components_text(start_date, end_date):

    diff_in_millis = (end_date - start_date).total_seconds() * 1000

    second = diff_in_millis / 1000 % 60
    minutes = diff_in_millis / (1000 * 60) % 60
    hours = diff_in_millis / (1000 * 60 * 60) % 24
    days = diff_in_millis / (1000 * 60 * 60 * 24) % 365
    years = diff_in_millis / (1000 * 60 * 60 * 24 * 365)

    return f"{years} años, {days} días, {hours:.2f} horas, {minutes:.2f} minutos, {second:.2f} segundos"


def adeviento2022(date):

    formato = "%Y/%m/%d %H:%M:%S"
    start_date = datetime.strptime("2022/12/01 00:00:00", formato)
    end_date = datetime.strptime("2022/12/24 23:59:59", formato)
    format_date = datetime.strptime(date, formato)

    if start_date <= format_date <= end_date:

        gifts = [
            "El programador pragmático",
            "while True: learn()",
            "Aprende Javascript ES9, HTML, CSS3 y NodeJS desde cero",
            "Patrones de Diseño en JavaScript y TypeScript",
            "Aprende Python en un fin de semana",
            "Regalo 6",
            "Regalo 7",
            "Regalo 8",
            "Regalo 9",
            "Regalo 10",
            "Regalo 11",
            "Regalo 12",
            "Regalo 13",
            "Regalo 14",
            "Regalo 15",
            "Regalo 16",
            "Regalo 17",
            "Regalo 18",
            "Regalo 19",
            "Regalo 20",
            "Regalo 21",
            "Regalo 22",
            "Regalo 23",
            "Regalo 24",
        ]

        end = datetime.strptime(date.split(" ")[0] + " 23:59:59", formato)
        day = int(date.split(" ")[0].split("/")[2])
        return f"El regalo del día es: {gifts[day - 1]} y el sorteo del día acaba en: {diff_time_components_text(format_date, end)}"

    intro = (
        "El calendario de aDEViento 2022 comenzará en:"
        if format_date < start_date
        else "El calendario de aDEViento 2022 ha finalizado hace:"
    )
    time_components = (
        diff_time_components_text(format_date, start_date)
        if format_date < start_date
        else diff_time_components_text(end_date, format_date)
    )
    return f"{intro} {time_components}"


print(adeviento2022("2022/12/05 20:27:56"))
print(adeviento2022("2022/12/01 00:00:00"))
print(adeviento2022("2022/12/24 23:59:59"))
print(adeviento2022("2022/11/30 23:59:59"))
print(adeviento2022("2022/12/25 00:00:00"))
print(adeviento2022("2022/10/30 00:00:00"))
print(adeviento2022("2022/12/30 04:32:12"))
print(adeviento2022("2020/10/30 00:00:00"))
print(adeviento2022("2024/12/30 04:32:12"))
