from datetime import datetime


def time_between_release(game1, game2):
    ZELDA_GAMES = {
        "The Legend of Zelda": "21/02/1986",
        "Zelda II: The Adventure of Link": "14/01/1987",
        "A Link to the Past": "21/11/1991",
        "Link's Awakening": "06/06/1993",
        "Ocarina of Time": "21/11/1998",
        "Zelda: Majora's Mask": "27/04/2000",
        "Oracle of Ages": "27/02/2001",
        "Oracle of Seasons": "27/02/2001",
        "Four Swords": "03/12/2002",
        "The Wind Waker": "13/12/2002",
        "Four Swords Adventures": "18/03/2004",
        "The Minish Cap": "04/11/2004",
        "Twilight Princess": "19/11/2006",
        "Phantom Hourglass": "23/06/2007",
        "Spirit Tracks": "07/12/2009",
        "Skyward Sword": "18/11/2011",
        "A Link Between Worlds": "23/11/2013",
        "Tri Force Heroes": "11/10/2015",
        "Breath of the Wild": "03/03/2017",
        "Tears of the Kingdom": "12/05/2023",
    }

    if game1 == game2:
        return "It's the same game"

    current_release_date = datetime.strptime(ZELDA_GAMES[game1], "%d/%m/%Y").date()
    new_release_date = datetime.strptime(ZELDA_GAMES[game2], "%d/%m/%Y").date()

    if current_release_date and new_release_date:
        start_date = min(current_release_date, new_release_date)
        end_date = max(current_release_date, new_release_date)

        years = end_date.year - start_date.year
        months = end_date.month - start_date.month
        days = end_date.day - start_date.day

        return f"Years: {years}, Months: {months}, Days: {days}"
    else:
        return "Invalid release date"


legend_of_zelda = "The Legend of Zelda"
tears_of_the_kindom = "Tears of the Kingdom"
adventure_of_link = "Zelda II: The Adventure of Link"

print(time_between_release(legend_of_zelda, tears_of_the_kindom))
print(time_between_release(tears_of_the_kindom, legend_of_zelda))
print(time_between_release(legend_of_zelda, adventure_of_link))
print(time_between_release(adventure_of_link, legend_of_zelda))
print(time_between_release(legend_of_zelda, legend_of_zelda))
print(time_between_release("Oracle of Ages", "Oracle of Seasons"))
