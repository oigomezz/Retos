# [Optimal Network Expansion][link]

You are presented with a network comprising N computers and M wired connections between them. Your objective is to optimize the network's connectivity using precisely K wires from your inventory. The aim is to maximize the number of computers that can be linked together within the given constraints. Your task is to determine and report the size of the largest network that can be formed by establishing these connections.

In the context of this problem, computers are considered connected if they share either a direct or indirect wired connection. It is worth noting that the value of K will always be less than the number of isolated (standalone) networks in the given configuration, and it may even be zero.

## Input format

- The first line contains three integers separated by a space: N, M, and K, where:
  - N is the number of computers in the network.
  - M is the number of wired connections between computers.
  - K is the number of wires at your disposal.
- The next M lines, each contain two integers, ai and bi, representing a wired connection between computers with IDs ai and bi.

## Output format

Your program should output a single integer representing the size of the largest network that can be formed after connecting K wires.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/optimal-network-expansion-de452a46/
