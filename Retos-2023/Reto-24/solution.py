def mcd(first_number, second_number):
    a = first_number
    b = second_number

    while a != 0 and b != 0:
        temp = b
        b = a % b
        a = temp
    return a + b

def mcm(first_number, second_number):
    return (first_number * second_number) // mcd(first_number, second_number)


print(mcd(56, 180))
print(mcm(56, 180))