# [Flight Tickets][link]

There are N cities in the country Byteland. Each city has some special value associated with it. All the cities are connected to one another either via direct flights or a series of connecting flights. There are a total of N-1 flights available and it is always possible to reach any city from any other city thus the structure of flights between the cities in Byteland forms a tree. The fare of flight between two cities is given by the distance between the two cities in the tree.

Now Rohan books flights between the two cities if and only if their special value is equal. He wants to book the cheapest and distinct k flights. He follows the following rules while booking flights:

- Two flights are distinct if their start city or destination city is different from other booked flights.
- Note that since Byteland is mysterious, booking of flight from the same city to the same city is also possible with a cost of 0.
- If Rohan books a flight from the city A to city B then he can't book any flight from the city B to city A.
- In the output, you need to print the price of the last flight that he would book. If it is impossible to book K flights then you need to print -1.

## Input format

- The first line contains two space-separated integers N and Kdenoting total number of cities and the total flights that Rohan needs to book.
- Each of the next N-1 lines contain 2 space separated integers u and v which denote that there exists a flight between the cities with number u and v.
- The next line contains N space-separated integers, where the i-th integer denotes Ci which denotes the special value associated with the city numbered i.

It is guaranteed the given input edges form a valid tree.

## Output format

Print a single integer denoting the answer.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tree-and-colored-nodes-c4f5bbe3/
