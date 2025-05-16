# [Bob and cities][link]

Bob is living in a city in which houses are arranged in NxM block.

The city is denoted by N strings having M characters such that '.' denotes house while '#' denotes forests.

Bob has to pay a certain amount LCost, RCost, UCost, DCost to move 1 step across left, right, up or down respectively.

Bob lives in a house having co-ordinates (Stx , Sty) (1-Based Indexing).

You are given Q tasks contains an integer X each. In each task, you have to find number of unique houses (including his house) can be travelled using the amount X.

## Input format

- First line contains two space separated integers N and M, denoting number of rows and columns respectively.
- Next N lines contain a string each containing M characters. (Note: Top left corner will denote {1,1})
- Next line containd four space separated integers denoting LCost, RCost, UCost, DCost respectively.
- Next line contains two space separated integers Stx and Sty, denoting position of Bob's house.
- Next line contains an integer Q denoting number of tasks.
- Next Q lines contain an integer X each, denoting the amount Bob have.

## Output format

For each task, output a single integer denoting the number of unique houses (including his house) Bob can visit using the amount X.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/bob-and-cities-dfc06921/
