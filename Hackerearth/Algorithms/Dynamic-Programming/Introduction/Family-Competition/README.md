# [Family competition][link]

Two families The Bakers and The Murtaughs are rival families and they are competing in a final round of the competition, which is to decide who of these two families are going to be the winners of the competition. The purpose of the competition being union and friendship of the families, the last competition requires both families to collaborate on getting the best result they can achieve.

They are playing volleyball like game. We can describe volleyball field as an x-axis, the net is located at point 0. Each of the Bakers is located in negative part of x-axis, so that xi < 0, it's -xi meters away from the net. And each of the Murtaughs is located in positive part of x-axis, so that xi > 0, it's xi meters away from the net. For each family member her age ai seconds since birth is known.

The goal of the game is to choose who should start the game and then make maximum possible number of ball throws.

The game proceeds as follows. At first one of the family members is given a ball. Any family member of any of two families can be given a ball. On each throw, player who has a ball throws it to one of the players of the other family, and so on.

A player can throw a ball only to the player of the opposite team, who is strictly older than her. Family members are not so strong, so each of them can throw a ball h meters from her location. Formally, player i can throw ball to player j, if sign(xi) != sign(xj), ai < aj and |xi - xj| <= h, where sign is a Sign function.

Find the maximum number of throws families can achieve.

## Input format

- First line of input contains two integers n and h — the total number of members in both families and the maximum distance they can make single throw on.
- Each of the next n lines consists of two integers ai and xi — age and location of the i-th family member.

## Output format

Output single integer: the maximum number of ball throws families can achieve.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/family-competition/
