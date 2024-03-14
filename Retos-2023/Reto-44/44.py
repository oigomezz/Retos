import random


class Halloween:
    TRICK = 1
    TREAT = 2


class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


def trick_or_treat(halloween, people):
    scares = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
    candies = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
    result = ""
    height = 0

    for person in people:
        if halloween == Halloween.TRICK:
            for _ in range(len(person.name.replace(" ", "")) // 2):
                result += random.choice(scares)

            if person.age % 2 == 0:
                result += random.choice(scares)
                result += random.choice(scares)

            height += person.height
            while height >= 100:
                result += random.choice(scares)
                result += random.choice(scares)
                result += random.choice(scares)
                height -= 100

        elif halloween == Halloween.TREAT:
            for _ in range(len(person.name.replace(" ", ""))):
                result += random.choice(candies)

            if person.age <= 10:
                for _ in range(person.age // 3):
                    result += random.choice(candies)

            if person.height <= 150:
                for _ in range(person.height // 50):
                    result += random.choice(candies)
                    result += random.choice(candies)

    return result


people = [
    Person("Brais", 35, 177),
    Person("Sara", 9, 122),
    Person("Pedro", 5, 80),
    Person("Roswell", 3, 54),
]

print(trick_or_treat(Halloween.TRICK, people))
print(trick_or_treat(Halloween.TREAT, people))
