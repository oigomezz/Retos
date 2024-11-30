class Money:
    FIVE = 5
    TEN = 10
    FIFTY = 50
    ONEHUNDRED = 100
    TWOHUNDRED = 200

    def get_coins(self):
        return [
            Money.TWOHUNDRED,
            Money.ONEHUNDRED,
            Money.FIFTY,
            Money.TEN,
            Money.FIVE,
        ]


def buy(code, money):
    products = {
        1: ("Agua", 50),
        2: ("Coca-Cola", 100),
        4: ("Cerveza", 155),
        5: ("Pizza", 200),
        10: ("Donut", 75),
    }

    if code in products:
        product = products[code]

        total_money = 0
        for coin in money:
            total_money += coin

        if total_money < product[1]:
            return (
                "El producto con código [{}] tiene un coste {}. Has introducido {}.".format(
                    code, product[1], total_money
                ),
                money,
            )

        pending_money = total_money - product[1]

        return (product[0], return_money(pending_money, []))

    return ("El producto con código [{}] no existe.".format(code), money)


def return_money(pending_money, money):
    if pending_money == 0:
        return money

    new_pending_money = pending_money
    new_money = money.copy()

    list_money = Money.get_coins(Money)

    for coin in list_money:
        if coin <= pending_money:
            new_pending_money -= coin
            new_money.append(coin)

    return return_money(new_pending_money, new_money)


print(buy(1, [Money.FIVE, Money.FIVE, Money.TEN, Money.TEN, Money.TEN, Money.FIVE]))
print(buy(3, [Money.FIVE, Money.FIVE, Money.TEN, Money.TEN, Money.TEN, Money.FIVE]))
print(
    buy(
        1,
        [
            Money.FIVE,
            Money.FIVE,
            Money.TEN,
            Money.TEN,
            Money.TEN,
            Money.FIVE,
            Money.FIFTY,
        ],
    )
)
print(buy(5, [Money.TWOHUNDRED]))
