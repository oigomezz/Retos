# [Left or Right][link]

A country X consists of N cities numbered 0 through N-1. The map of this country can be represented as a cycle — for each valid i, city i has exactly two neighboring cities (i+1)%N and (i-1+N)%N.

The cities in the country are broadly categorized into different types. For each valid i, the type of city i is denoted by Ai.

A person called Suarez wants to travel between some pairs of the cities. You are given Q queries. In each query, Suarez wants to travel from city number Y to a city of type Z. Also, he wants to travel only in a given direction along the cycle.

The direction is represented by a letter — L or R. If it's L, Suarez may only move from city i to city (i-1+N)%N for each valid i. If it's R, he may only move from city i to city (i+1)%N.

You need to find the minimum number of steps Suarez needs to take to reach a city of type Z if he starts moving from city Y in the given direction (he can take zero steps). In one step, Suarez can move from his current city to a neighboring city.

If Suarez can never reach a city of type Z for a given query, print 1 instead.

## Input format

- The first line of the input contains two space-separated integers N and Q. The next line contains N space-separated integers, where the i-th of these integers represents Ai.

- Each of the following Q lines describes a query in the format Y Z D, where Y is an integer denoting the number of the starting city, Z is an integer denoting the type of a target city and D is a letter ('L' or 'R') denoting the direction along the cycle.

## Output format

For each query, print a single line containing one integer — the answer to the query.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/left-or-right-92c0b54c/
