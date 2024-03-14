class LostNumbersException(Exception):
    def __init__(
        self,
        message="El listado no puede poseer repetidos ni estar desordenado, y debe tener mínimo 2 valores.",
    ):
        self.message = message


def lost_numbers(numbers):
    if len(numbers) < 2:
        raise LostNumbersException()

    try:
        first = numbers[0]
        last = numbers[-1]
        asc = first < last

        prev = None
        for number in numbers:
            if prev is not None:
                if (asc and number <= prev) or (not asc and number >= prev):
                    raise LostNumbersException()
            prev = number

        lost = []
        for number in range(first, last + 1) if asc else range(last, first + 1):
            if number not in numbers:
                lost.append(number)

        return lost 

    except LostNumbersException as e:
        print(e.message)


print(lost_numbers([1, 3, 5]))
print(lost_numbers([5, 3, 1]))
print(lost_numbers([5, 1]))
print(lost_numbers([-5, 1]))
print(lost_numbers([1, 3, 3, 5]))
print(lost_numbers([5, 7, 1]))
print(lost_numbers([10, 7, 7, 1]))
