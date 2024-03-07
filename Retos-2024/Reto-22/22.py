import os


def calculate(file_path):
    if os.path.isfile(file_path):
        f = open(file_path)
        number = None
        result = None
        last_operator = None
        line = f.readline().strip()
        while line:
            if line == "+" or line == "-" or line == "*" or line == "/":
                last_operator = line
            else:
                number = float(line)
                if result is None:
                    result = number
                else:
                    if last_operator == "+":
                        result += number
                    elif last_operator == "-":
                        result -= number
                    elif last_operator == "*":
                        result *= number
                    elif last_operator == "/":
                        result /= number
                last_operator = None
            line = f.readline().strip()
        f.close()

        return result
    else:
        print("El archivo no existe")


path_name = "Retos-2024/Reto-22/example.txt"
print(calculate(path_name))
