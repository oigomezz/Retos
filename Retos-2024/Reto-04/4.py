def main(num):
    for number in range(1, num):
        if is_prime(number):
            print(number)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

main(101)
