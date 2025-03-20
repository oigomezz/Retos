# [Development Cost][link]

A country is represented as a matrix of the size N x M and each cell is considered to be a city.

There are Q missions and you are required to accomplish K missions to receive the tourist certification. In each mission, you are given a source and destination and you need to travel from source to destination.

Each city contains a development cost that depicts the state of development of the city. The development cost of a mission is considered to be the maximum development cost in the path between source and destination.The overall development cost for the certification is the maximum development cost of all the accomplished missions. Your task is to minimize the overall development cost to achieve the certificate.

Note:

- A path can visit a particular cell multiple times. It is possible to go up, down, left, and right from any cell.
- It is not necessary to accomplish the first K missions. You can accomplish any K missions out of the given Q missions.
- It is not necessary to travel from a source to a destination by using the shortest path. You are allowed to take any path to travel from a source to a destination.

## Input format

- First line: Four integers N, M, Q, and K respectively.
- Next N lines: M integers, where the j-th integer on the line representing Aij.
- Next Q lines: Four integers X[source], Y[source], X[destination] and Y[destination] respectively.

**Note:** It is guaranteed that the source city and destination city do not coincide for a mission.

## Output format

Print the minimum value of the overall development cost in accomplishing exactly K missions.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/dangerous-path-467b0dc7/
