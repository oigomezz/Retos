# [Decaying Roads][link]

There is a City having some set of roads where each road has the same source and the same destination.There are N trucks and M roads in the city.You are given K permits in the city(in the form of X and Y) which indicates that a truck X is permitted to travel on Road Y.

Each road has a restriction on the number of trucks it can allow to travel on it.This restricted number is known as Capacity[i].

Due to the poor condition of the roads, every year 1 particular road's capacity reduces by a number P. The data is known for Z years.

For each year before the reduction takes place,you need to predict the maximum number of trucks that can travel in the city.

## Input format

- First line contains 3 integers N , M and K.
- Next K lines contain 2 integers X and Y denoting that Xth truck is permitted on Yth road.
- Then there is an array of size M consisting of Capacity[i].
- Then there is an integer Z (number of years for which the information is provided).
- Then Z lines contain 2 integers R and P denoting Road R's capacity reduces by P.

## Output format

Print Z lines containing the maximum number of trucks that can travel in the city.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/maximum-flow/practice-problems/algorithm/decaying-roadsnov-easy-8e930584/
