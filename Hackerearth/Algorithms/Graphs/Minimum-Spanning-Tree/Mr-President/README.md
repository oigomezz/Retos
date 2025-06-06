# [Mr. President][link]

You have recently started playing a brand new computer game called "Mr. President". The game is about ruling a country, building infrastructures and developing it.

Your country consists of N cities and M bidirectional roads connecting them. Each road has assigned a cost of its maintenance. The greatest achievement in the game is called "Great administrator" and it is given to a player who manage to have all cities in the country connected by roads in such a way that it is possible to travel between any two cities and that the sum of maintenance costs of these roads is not greater than K.

This is very hard to accomplish, but you are very close to do it. More precisely, you have just discovered a new method of transforming standard roads into super roads, with cost of maintenance just 1, due to their extreme durability.

The bad news is that it is very expensive to transform a standard road into a super road, but you are so excited that you are going to do it anyway.

In addition, because you have a lot of other expenses, you also want to first demolish as many roads as possible in order to safe some money on their maintenance first and then start working on getting the achievement. You can demolish any road in the country and that operation does not cost you anything.

Because you want to spend the absolutely minimum money in order to get the achievement, you are interested in the smallest number of transformations of standard roads into super roads in such a way that you can do that.

## Input format

- In the first line there are 3 integers N, M and K denoting the number of cities in the country, the number of roads in it and the desired sum of costs of maintenance.
- M lines describing these roads follow.
  - In each of them there are 3 integers A, B and C, where A and B denote the endpoints of the road while C denotes the cost of its maintenance.

## Output format

In a single line, output the minimum number of roads which need to be transformed in order to get the achievement. If you cannot do it no matter what, output -1.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/mr-president/
