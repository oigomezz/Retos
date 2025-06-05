# [Travelling Tom][link]

Tom is visiting the country Hackerland. Hackerland has n cities and m bi-directional roads. There are k types of tokens. Token i costs Ci. The costs of the tokens are such that for all 2 <= i <= k, Ci >= 2C(i-1). For each road, you need to have a particular set of tokens, if you want to travel it. Note that you don't have to give the tokens, you just need to show them. Thus, one token can be used at any number of roads, where it is required. Tom wants to select a set of tokens, such that using them, he can go from any city to any other city. You have to help him minimize the total cost of tokens he buys.

## Input format

- The first line contains three space separated integers, n m and k.
- The second line contains k space separated integers, where the i-th integer denotes the price of i-th token, i.e. Ci.
- i-th of the next m lines contains three integers ui,vi,li, where li is the number of tokens required by the i-th road, followed by li indices denoting the tokens required. This road connects cities ui and vi.

## Output format

Print one integer containing the minimum cost of tokens Tom has to buy, such that he can travel from any city to any other city. If it is impossible to choose such a set of tokens, print 1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/travelling-tom-7eadedb7/
