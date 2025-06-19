# [Salesmen problem][link]

You are working in a salesmen company as a programmer.

There are n towns in your country and m directed roads between them. Each road has a cost person should spend on fuel. The company wants to sell goods in all n towns. There are infinitely many salesmen in the company. We can choose some positive number of salesmen and give a non-empty list of towns to each of them. Towns from the list are the towns to sell goods in. Each salesman will visit all the towns in his list in this particular order in cycle (after the last town he will return to the first town and so on). Salesman can visit other towns on his way but he will not sell goods in these towns. Two salesmen cannot sell goods in one town because it will attract unnecessary attention to your company. But for every town there must be a salesman who sell goods in this town. If salesman's list of towns consists of exactly one town then he should pay fee to stay in this town each month (each town has its own fee) or he should go for a round trip and spend money on fuel.

Your task is to calculate the minimal amount of money company must spend monthly to achieve its goals. We will assume that every salesman will spend a month to make one cycle.

## Input format

- The first line of input contains two integers n and m - number of towns and number of directed roads between them respectively.
- The second line contains n numbers ai - monthly fee for i-th town.
- Next m lines describe roads. Each description looks like u v cost and describes a road from town u to town v with assigned cost cost. It is guaranteed that there are no two roads between the same pair of towns in the same direction.

## Output format

Print one integer - the minimal amount of money to spend.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/practice-problems/algorithm/salesmans-problem/
