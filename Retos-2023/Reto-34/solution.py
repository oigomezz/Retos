def chinese_zodiac(year):
    elements = [
        "madera", 
        "fuego", 
        "tierra", 
        "metal", 
        "agua"
    ]
    
    animals = [
        "rata",
        "buey",
        "tigre",
        "conejo",
        "dragón",
        "serpiente",
        "caballo",
        "oveja",
        "mono",
        "gallo",
        "perro",
        "cerdo",
    ]

    if year < 604:
        return f"{year}: El ciclo sexagenario comenzó en el año 604."

    sexagenary_year = (year - 4) % 60
    element = elements[(sexagenary_year % 10) // 2]
    animal = animals[sexagenary_year % 12]

    return f"{year}: {element} {animal}"


print(chinese_zodiac(1924))
print(chinese_zodiac(1946))
print(chinese_zodiac(1984))
print(chinese_zodiac(604))
print(chinese_zodiac(603))
print(chinese_zodiac(1987))
print(chinese_zodiac(2022))
