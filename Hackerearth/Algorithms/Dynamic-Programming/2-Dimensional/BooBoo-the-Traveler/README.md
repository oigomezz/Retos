# [BooBoo the traveler][link]

BooBoo is a smart baby who likes to travel around cities. And he is on a trip to Europe right now! Smart that he is, he has made a list of N cities to visit, and for each city he has M popular places to visit in each city. But being a baby, he does get exhausted pretty quickly and thus plans his trip in an all together different way. For a trip to be successful and non exhausting, BooBoo decides that he will visit exactly one city everyday and in each city, he will visit only one of the M popular places. He has also decided that it's optimal to move across the cities in order 1,2,...,N.

Now there's one more constraint related to travelling: Cost! Since Europe trips are pretty much popular, there are special travelling schemes in offer for the travelers. Let's assume you are currently at the j-th place in city i and you plan to move to k-th place of the next city. This move is only possible if and only if the lowest prime factor of both j and k is same. The cost for any such valid move is equal to Aij if j = k, otherwise the cost is equal to Bij. 1 is treated as an exception: we assume that all j can lead to k if k = 1. For the first city, you can visit any place you wish to start with without any restriction.

BooBoo has other trips lined up and hence would like you to help him minimize the cost of his successful and non exhausting Europe trip. Can you help him out?

## Input format

- The first line contains two space separated integers N and M.
- The next line contains S0,P,Q and R, which are inputs to the generator for matrix A.
- The next line contains W0,X,Y and Z, which are inputs to the generator for matrix B.

## Output format

Output only one integer, the minimum cost of travelling across all N cities.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/booboo-and-travelling-circuits/
