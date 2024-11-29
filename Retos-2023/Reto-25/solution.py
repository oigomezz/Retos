# 1
print("**** 1 ****")

for index in range(1, 101):
    print(index)

# 2
print("**** 2 ****")

list(map(lambda index: print(index), range(1, 101)))

# 3
print("**** 3 ****")

whileIndex = 1

while whileIndex <= 100:
    print(whileIndex)
    whileIndex += 1

# 4
print("**** 4 ****")


def print_100(index):
    if index <= 100:
        print(index)
        print_100(index + 1)


print_100(1)
