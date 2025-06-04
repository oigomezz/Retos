# [Candy Game][link]

There are N candies in a room labelled from 1 to N and there are N - 1 directed path between these candies such that every candy has at least 1 path leading to the candy or away from it.

K and L want to eat all the candies in the room but they don't know where to start.

If K starts with the candy labelled c (1 <= c <= N), then he can eat all the candies which can be reached from the position of the candy c. Similarly, if L starts with the candy labelled d (1 <= d <= N), then he can eat all the candies which can be reached from the position of the candy d. Note that both, K and L, can start from the same candy position.

Now, they will be able to eat all the candies in the room if there exist candy positions c and d such that any other candy in the room can be eaten by at least one of them. In order to make this possible, they want to change the direction of some number of paths. You have to calculate the minimum number of paths that need to be changed so that K and L can eat all the candies.

## Input format

- The first line of input contains the number of candies, N(1 <= N <= 3000).
- Each of the next N-1 lines contains 2 space separated integers ai and bi (1 <= ai,bi <= N; ai != bi) denoting that there exists a directed path from candy ai to candy bi. Candies are labeled from 1 to N.

## Output format

In the only line of output print the minimum number of paths that need to be changed so that K and L can eat all the candies.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/candy-game/
