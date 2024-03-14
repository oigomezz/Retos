import re


def temperature_converter(degrees):
    formatter = "{:.2f}"

    try:
        if "°C" in degrees:
            celsius_degrees = float(re.sub(r"\s|°C", "", degrees))
            return f"{formatter.format((celsius_degrees * 9/5) + 32)}°F"

        elif "°F" in degrees:
            fahrenheit_degrees = float(re.sub(r"\s|°F", "", degrees))
            return f"{formatter.format((fahrenheit_degrees - 32) * 5/9)}°C"

    except Exception as e:
        return "Invalid input: " + str(e)

    return "Invalid input."


print(temperature_converter("100°C"))
print(temperature_converter("100°F"))
print(temperature_converter("100C"))
print(temperature_converter("100F"))
print(temperature_converter("100"))
print(temperature_converter("100"))
print(temperature_converter("- 100 °C "))
print(temperature_converter("- 100 °F "))
print(temperature_converter("100A°C"))
print(temperature_converter("100A°F"))
print(temperature_converter("°C"))
print(temperature_converter("°F"))
