def check_math_exp(expression: str) -> bool:
    components = expression.split(" ")

    if len(components) < 3 or len(components) % 2 == 0:
        return False

    check = True

    for index, component in enumerate(components):
        if index % 2 == 0:
            try:
                float(component)
            except ValueError:
                check = False
                raise
        else:
            check = component in ["+", "-", "*", "/", "%"]

        if not check:
            return False

    return check


print(check_math_exp("3 + 5"))
print(check_math_exp("3 a 5"))
print(check_math_exp("-3 + 5"))
print(check_math_exp("- 3 + 5"))
print(check_math_exp("-3 a 5"))
print(check_math_exp("-3+5"))
print(check_math_exp("3 + 5 - 1 / 4 % 8"))
