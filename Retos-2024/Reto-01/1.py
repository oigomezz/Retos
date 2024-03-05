def fizzbuzz(num):
    for number in range(num):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        # trunk-ignore(git-diff-check/error)
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)


fizzbuzz(1000)
