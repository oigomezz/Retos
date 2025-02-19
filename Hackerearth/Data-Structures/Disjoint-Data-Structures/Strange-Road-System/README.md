# [Strange Road System][link]

Marichka will visit HackerLand, the country with N (1 <= N <= 10⁵) cities, on her spring holidays. She feels very excited because of this.

During the next Q days one of the two following events happens.

- 1 U V P (1 <= U <= N, 1 <= V <= N, 1 <= P <= 10⁹) --- hackers build a new bidirectional road with happiness points $P$ between cities U and V.

- 2 U V (1 <= U <= N,1 <= V <= N) --- Your task is to answer the query. You are given cities numbers --- U and V, and your task is to find maximum happiness Marichka can get after travelling in some way(maybe through some intermediate cities) between cities U and V. If there is no way to get from the city U to the city V between them, then simply output -1.

If Marichka's happiness before traversing some road was X and road's happiness points are Y, then after traversing it Marichka's happiness will be equal to X ⊕ Y. Marichka can traverse one road many times. She also can visit some city many times during her travel.

Initially, there are no roads in HackerLand.

## Input format

- The first line consists of two integers N and Q --- the number of cities and the number of days, respectively.
- Next Q lines contain information about events in the format described above.

## Output format

For each query of the second type, print only one integer in the single line --- maximum happiness Marichka can get after travelling in some way between cities U and V. It is guaranteed that there exists at least one such query.

[link]: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/strange-road-system-5094b65a/
