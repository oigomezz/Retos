# [Roads reconstruction][link]

The HackerEarth land consists of N cities and M roads connecting them. Every city has at-least one road connected to it. There can be more than one road connecting pair of cities and there can be a road which connects the city with itself. There can be no way to connect from one city to some other city using only these roads.

The mayor has decided to order the reconstruction of the roads in the city, every road has a specific cost to be reconstructed and please note for every city there must exist at-least one road connected to it which is reconstructed.

You are given an array A of length N where Ai denotes the cost to bear if a road connected to i-th city is reconstructed. Means if there is a road connection city i,j then the cost to bear for that road will be Ai + Aj.

The total cost of reconstruction will be evaluated as follows:

- Cost of all the roads reconstructed + Cost to bear due to cities which have these reconstructed roads.

Aim is to minimize Z = total cost of reconstruction.

## Input format

- First line contains two space-separated integers N, M.
- Next line contains N space-separated integers denoting the array A.
- Next M lines contain three space-separated integers u,v,w denoting a road connecting city u and v which has w cost for reconstruction.

## Output format

- In the first line print K+1 space-separated integers where K is the count of roads you have selected for reconstruction.
  - First integer should always be K (<=M).
  - Next K integers are the indices of the roads selected for reconstruction in any order. Roads are numbered starting from one in order of their appearance in the input.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/approximate/roads-reconstruction-29b8a191/
