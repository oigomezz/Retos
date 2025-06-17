# [Oliver and the Game][link]

Oliver and Bob are best friends. They have spent their entire childhood in the beautiful city of Byteland. The people of Byteland live happily along with the King.

The city has a unique architecture with total N houses. The King's Mansion is a very big and beautiful bungalow having address = 1. Rest of the houses in Byteland have some unique address, (say A), are connected by roads and there is always a unique path between any two houses in the city. Note that the King's Mansion is also included in these houses.

Oliver and Bob have decided to play Hide and Seek taking the entire city as their arena. In the given scenario of the game, it's Oliver's turn to hide and Bob is supposed to find him.

Oliver can hide in any of the houses in the city including the King's Mansion. As Bob is a very lazy person, for finding Oliver, he either goes towards the King's Mansion (he stops when he reaches there), or he moves away from the Mansion in any possible path till the last house on that path.

Oliver runs and hides in some house (say X) and Bob is starting the game from his house (say Y). If Bob reaches house X, then he surely finds Oliver.

Given Q queries, you need to tell Bob if it is possible for him to find Oliver or not.

The queries can be of the following two types:

- 0 X Y : Bob moves towards the King's Mansion.
- 1 X Y : Bob moves away from the King's Mansion

## Input format

- The first line of the input contains a single integer N, total number of houses in the city.
- Next N-1 lines contain two space separated integers A and B denoting a road between the houses at address A and B.
- Next line contains a single integer Q denoting the number of queries.
- Following Q lines contain three space separated integers representing each query as explained above.

## Output format

Print "YES" or "NO" for each query depending on the answer to that query.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/oliver-and-the-game-3/
