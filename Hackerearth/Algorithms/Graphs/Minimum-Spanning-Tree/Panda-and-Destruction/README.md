# [Panda and Destruction][link]

There is a country which is infected by virus. It has many cities and some cities are connected to other cities. In order to prevent virus from spreading Panda plans on destroying the connection between all the cities. Panda has got a power called pimogio. Using this power he can destroy any city, which results in destruction of all connections from this city. For destroying one city, Panda requires one unit pimogio power. Panda's final aim is to isolate all the cities. In order to do so, Panda follows a simple approach, he keeps on destroying the city with most number of connections in it at that moment.

Since Panda is weak in calculation, please help him in finding out the units of pimogio power required by him to achieve his aim. There cannot be multiple connections between two cities i.e. two cities can have only one road connected to them.

**Note:** If there are multiple cities with highest connections, destroy the city with the lowest index.

## Input format

- The first line will contain 2 space separated integers N and M, where N is the number of cities in Panda's town and M is the number of connections that the cities have.
- Next M lines follow, each line consists of two integers A and B, specifying that city A has a connection with city B and B has a connection with the city A.

## Output format

For each test case, output the minimum energy that Panda requires to achieve his aim.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/panda-and-destruction/
