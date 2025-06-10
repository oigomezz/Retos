# [Route Planning][link]

A city contains N stations. Also in the city circulate M buses. The i-th bus has an itinerary consisting of ti stations: si1, si2, ..., sit. At moment 0 it is at the station si1, and then each minute he travels to the next station. When it reaches the end it goes back to the begging and starts again. At moment 0 you are at station 1. If at any moment you and a bus are at the same station, you can get on it and travel with it. You can get off at any station. The same station can appear multiple times in the itinerary of the bus, but not adjacent to each other (in particular, the last station is adjacent to the first). You can only travel by bus. You are interested in finding the minimum amount of time you need to get to each station, or state that it is impossible.

You can only travel in one bus at a time, but you can use multiple buses to reach your destination. There can be multiple buses at the the same station at the same time. Getting in and off a bus is instantaneous.

## Input format

- The first line contains 2 integers N and M - the number of stations and the number of buses respectively.
- Each of the next M lines contain an integer ti followed by ti integers si1,si2,...,sit - the itinerary of a bus.

## Output format

Print N-1 numbers - the i-th number is the minimum amount of time needed to reach the (i+1)th station, or 1 if it is impossible.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/route-planning-c6409134/
