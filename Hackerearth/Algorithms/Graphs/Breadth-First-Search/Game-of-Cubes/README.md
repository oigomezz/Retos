# [Game of Cubes][link]

Alice and Bob are playing a game. In this game small cubes are placed over each other, forming a cuboid of length B, height L and breadth 1. The special property in these cubes is that adjacent cubes always form a cluster.

Note that a cluster requires a support, otherwise due to gravity it will fall down.

So, a cluster not having support will fall down due to gravity. While falling, it would not change it's shape. If any cube in this cluster comes in contact with cube from another cluster or ground, it will stop falling.

Now the game is as follows:

Alice and Bob alternate turns, Alice starting first. In each move of his/hers, the player would choose a height and throw an arrow. Alice throws from left to right, and Bob from right to left. If the arrow hits a cube, the cube and arrow both will be destroyed. If due to destruction of a cube, the cuboid becomes unstable, it will stabilise on it's own.

Given the moves of Alice and Bob, can you print the final state of the cuboid.

Note that, the testdata is such that, at any point of time, no two clusters will be falling at the same time. Also, initially, the cuboid is in the stable state.

## Input format

- First line contains two space separated integers denoting L and B.
- Each of the next L lines contain B characters each.
- Each character is either 'x' or '.' , denoting the presence or absence of a cube at that position.
- Next line contains N, the number of moves.
- Next line contains N integers, each integer denoting a height at which the arrow was thrown.

The moves are alternative, first move being made by Alice.

## Output format

Print the final state of the cuboid.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/game-of-cubes-43/
