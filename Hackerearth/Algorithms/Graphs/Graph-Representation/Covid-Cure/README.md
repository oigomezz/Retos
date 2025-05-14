# [Covid Cure][link]

In the Disneyland which consists of N cities and M connecting roads, you being the Mayor is planning to build new Hospitals to cure COVID - 19.

Every hospital which will be built in different cities, has two parameters associated with them.

- Patient capacity : Represented by array B.
- Establishment cost : Represented by array C.

So, Ci and Bi, denotes the capacity and establisment cost of hospital which will be built in the i-th city.

Due to spreading nature of virus we have following constraints on the establishment of hospitals.

- No two hospitals should be directly connected via a road.
- At-most one hospital can be built in a city.

You have to choose K cities to establish hospitals say represented by array A, such that the value of Z is maximized.

Z = Σ B[A[i]] - Σ C[A[i]]

## Input format

- First line contains two space-separated integers N,M.
- Next M lines contains two space-separated integers u,v denoting a direct road between city u and v.
- Next line contains N space-separated integers denoting array B.
- Next line contains N space-separated integers denoting array C.

## Output format

- Print an integer K ( >= 1) denoting the number of cities you choose to build hospitals.
- In next line print K space-separated integers denoting the index of selected cities.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/approximate/covid-cure-2-47ec0ade/
