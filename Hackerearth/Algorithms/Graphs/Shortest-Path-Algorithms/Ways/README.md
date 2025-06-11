# [Ways][link]

Amit and his wife Shweta are in Singapore for their honeymoon. Shweta wants to visit every hotel present there. Amit and Shweta are in their hotel and Amit is planning out how can he fulfill Shweta’s wish.

There are N hotels there(they are staying at the hotel No. 1). There are exactly M roads connecting those hotels (It is guaranteed that any hotel can be visited from any other by roads). Each road has its length. Every day the couple visits exactly one unvisited hotel and come back. Amit wants to take the shortest distance to get to any hotel from his hotel(they use the same path to get back to their hotel).

But there is a problem , Singapore government has announced that the tourists have to choose N-1 roads to move in the city i.e Amit has to choose total N-1 roads such that they can visit all the other hotels . Also path taken to reach any other hotel from their hotel should be the shortest. So in how many ways can Amit choose such N-1 roads.

## Input format

- First line contains the number of test cases T. Then T test cases follow.
- First line of each test cases contains N and M, the number of hotels and roads respectively.
- Next M lines contains A B C which denotes that there is a road of length C between hotels A and B.
- The couples are staying in Hotel No. 1.

## Output format

Print the number of ways modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/ways/
