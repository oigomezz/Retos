import time


def countdown(start: int, seconds: int):

    if (
        isinstance(start, int)
        and isinstance(seconds, int)
        and start > 0
        and seconds > 0
    ):
        for number in range(start, -1, -1):
            print(number)
            time.sleep(seconds)
        print("Boom!!! 💥")
    else:
        raise ValueError("Los parámetros tienen que ser enteros positivos")


countdown(10, 1)
