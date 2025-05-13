# [Utkarsh in Gardens][link]

Utkarsh has recently put on some weight. In order to lose weight, he has to run on boundary of gardens.
But he lives in a country where there are no gardens. There are just many bidirectional roads between cities.

Due to the situation, he is going to consider any cycle of length four as a garden. Formally a garden is considered to be a unordered set of 4 roads {r0, r1, r2, r3} where ri and ri+1 mod 4 share a city.

Now he wonders how many distinct gardens are there in this country.

## Input format

- The first integer contains N, the number of cities in the country.
- It is followed by space separated elements of N\*N binary matrix G.

## Note

- G[i][j] = 1 denotes there is a road between ith city and jth city.
- A pair of cities has atmost one road connecting them.
- No road connects a city to itself.
- G is symmetric.

## Output format

Print the total number of gardens.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/utkarsh-in-gardens-february-easy/
