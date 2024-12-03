import re

url = "https://retosdeprogramacion.com?year=2023&challenge=0&languaje=python"

components = url.split("&")
params = []

for component in components:
    if "=" in component:
        param = component.split("=")
        if len(param) == 2 and param[1] != "":
            params.append(param[1])

print(params)


# Solución con una expresión regular
params = []
regex = r"=([a-zA-Z0-9._%-]+)"
params = re.findall(regex, url)
print(params)
