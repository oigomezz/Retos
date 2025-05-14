# [Station Pairs][link]

Alice lives in a city having N stations connected by M railway tracks. Each track connects two distinct stations and no two tracks connect the same pair of stations. We can go from any station i to any station j where 1 <= i,j <= N, if there is a railway track between them. The distance between two stations is the minimum possible number of railway tracks on the path between them.

Alice wants to add one new track in the city. But she does not want to decrease the distance between her home station X and the office station Y.

Alice gave you a task to find the number of unordered pairs of two distinct stations that are not connected initially, such that if the new track between these two stations is built, the distance between stations X and Y won't decrease.

Note: There always exists a path between station i to station j, where 1 <= i,j <= N.

## Input format

- The first line contains an integer T, denoting the number of test cases.
- The first line of each test case contains four integers N, M, X and Y, denoting the total number of stations, the railway tracks, the home and office stations respectively.
- The next M lines represent the two integers A and B, such that there is a railway track from station A to station B.

## Output format

For each test case, find the total number of pairs of stations, such that adding a new track does not decrease the distance between X and Y.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/station-pairs-8c901658/
