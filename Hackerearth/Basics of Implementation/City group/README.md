# Excursion

You are living in a town consisting of N cities. Furthurmore, in this town there are K city-groups. You can reach any city from any city in a same city-group instantaneously. you can go from any city in ith city-group to any city in i+1th city-group in 1 second and from any city in i+1th city-group to any city in ith city-group in 1 second for each i between 1 and K-1, you can also go from any city in first city-group to any city in Kth city-group in 1 second and from any city in Kth city-group to any city in first city-group in 1 second.

You have been given Q queries each containing two cities X and Y. For each query, you have to print the minimum time it takes to reach city Y from city X.

Each city-group has a city which does not have a number (i.e. it is not one of the N cities mentioned above). you can visit those cities in the middle of your trip between cities X and Y given in queries.

## Input format

- First line of input will consists of two integers N and K denoting total number of cities and city groups.
- Next K lines will consists of information regarding city-groups.
  - First integer in these K lines will consists of number of cities Si belonging to that city-group.
  - Next Si integers for each line will consists of cities belonging to ith city-group.
- Next line will consists of integer Q denoting total number of queries.
  - Next Q lines will consists of two cities X and Y.

## Output format

For each of the query, print minimum time needed to reach city Y from city X.
