# Monk And His Unique Trip

Monk plans to visit Graphland. There are N cities and M one-way roads in Graphland. These cities are divided into various states. Cities of Graphland are partitioned into states in a unique way. For any two cities A and B, if it is possible to go from A to B and then return to A, they belong to the same state.

Graphland has inter state tax rule applicable. While passing through road between two cities belonging to different states, Monk has to pay a road tax of 1 dollar. For traveling on roads connecting cities in the same state, he will not be charged any tax. It is ensured that there is no road from any city to itself. It is also ensured that there will not be more than one one-way road from a city to another. Monk, being a foreigner to Graphland, is not aware of this tax rule. He just picks a source city and a destination city and he will travel between these two cities. Monk ensures that it is possible to reach the destination city from source using these one-way roads.

Monk can pick any two cities as source and destination respectively where it is ensured that destination is reachable from source using the roads. But he can take any of the possible paths for reaching the destination. Can you tell him the minimum amount of money he needs to bring so that he faces no issue in traveling no matter on whichever path he travels.

## Input format

- The first line contains two space-separated integers N and M denoting the number of cities in Graphland and number of one-way roads in Graphland respectively.
- The next M lines contain two space separated integers U[i] and V[i] which denotes that there is a one way road from U[i] to V[i].

## Output format

Output a single integer denoting the minimum money he needs to bring for traveling in Graphland.
