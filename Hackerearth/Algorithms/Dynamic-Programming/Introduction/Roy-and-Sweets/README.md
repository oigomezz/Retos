# [Roy and Sweets][link]

Its Diwali time and Little Roy's family is having a lot of guests. Guests come in families. Each guest family has M members. Roy's task is to serve sweets to them. Roy has N different sweets and each sweet has some specific sweetness level S and quantity Q.

Each guest family will give R rupees (as a token of gratitude) to Roy if following conditions are satisfied:

1. The sweetness level of sweet served is greater than or equal to the members in the guest family
2. Every member should get sweet of one particular sweetness level
3. Every member should get equal quantity of sweets

where R = 100 \* Quantity of sweet(s) each member had.

After each guest family has left, Roy's Mom makes sure that the quantity of sweets that guest family had is restored to its original value.

Your task is to find R - maximum amount in rupees Roy has after all the guests have come and left.

## Input format

- First line will contain integer N - number of different sweets.
- Next N lines will contain two space separated integers S and Q, S - Sweetness level of the sweet (this will be distinct for each sweet), Q - Quantity of that sweet
- This is followed by an integer G - number of guest families.
- Next G lines will contain integer M, indicating number of members in the guest family.

## Output format

Print integer R in single line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/roy-and-sweets/
