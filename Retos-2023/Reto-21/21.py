import threading


def async_sum(number_one, number_two, seconds, result):
    threading.Thread(
        target=lambda: delayed_sum(number_one, number_two, seconds, result)
    ).start()


def delayed_sum(number_one, number_two, seconds, result):
    import time

    time.sleep(seconds)
    result(number_one + number_two)


async_sum(5, 2, 10, lambda result: print(result))
async_sum(1, 3, 5, lambda result: print(result))
