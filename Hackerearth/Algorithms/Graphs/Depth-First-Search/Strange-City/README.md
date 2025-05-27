# [Strange City][link]

Anchal lives in a city which has N​ ice cream parlours. The city has N-1 connections such that every ice cream parlour can be reached from every other ice cream parlour. Each parlour has only one type of ice cream with cost Ci​ for each 1 <= i <= N​. Anchal has Q​ queries with each query specifying a city R​ and two integers X and Y. In every query she wants to reach the same destination ice cream parlour D. Anchal wants to calculate the number of cities from which she can start her journey and reach the destination city D​ along the shortest path between the source and the destination city such that city R lies in its path and the sum of ice creams for these three cities lie between ​X and Y (Both inclusive).

**Note:** City D, City R and the city from which Anchal starts are pairwise distinct.

## Input format

- First line consists of three space separated integers N, Q and D as described above.
- Second line consists of N space separated integers with i-th integer denoting Ci as described above.
- Next N-1 lines each consist of 2 space separated integers U and V denoting there is a bidirectional path from ice cream parlour U to V and vice versa.
- Each of the following Q lines contain three space separated integers IN1, IN2 and IN3 describing one query. Lets define last as the answer of the previous query (If its first query then last = 0). The parameters of the query can be calculated by:

  - R = IN1 ⊕ last
  - X = IN2 ⊕ last
  - Y = IN3 ⊕ last

  where ⊕ is the symbol for logical XOR.

## Output format

For each query, print the answer to it on a separate line

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/strange-city-ea5f4994/
