# [Fruits in a state][link]

There are n states in a country. The states are connected to each other by undirected borders and there are total n - 1 borders between different pairs of states. These borders form a tree. The strength of a border i is ten[i].

Each state grows some fruits. Initially, there are no fruits in any states. The rate at which a fruit is grown in state i is R[i] per unit time. A country that is defined as a tree of connected states is considered rich at an instant if all the states contain at least X fruits.

A company wants to buy these fruits. It buys fruits from the state that contains the lowest production rate in the country and it visits a country only if it is rich. If there are multiple such countries, the company randomly chooses one state and buys from it.

You are required to answer q queries that are represented as follows:

The i-th query consists of three space-separated integers a[i], b[i], c[i]. They allow you to generate D[i], T[i] and X[i] as D[i] = a[i]^ans[i-1], T[i] = b[i]^ans[i-1], and X[i] = c[i]^ans[i-1], where ans[i] is the answer to the i-th query and ans[0] = 0.

At t = 0, borders whose strength value is greater than D[i] splits apart and the remaining connected states form separate countries. Your task is to determine the total number of fruits that the company can collect at time T[i].

**Note:** Each query is independent in nature.

You are required to answer these queries online because the input of the next query depends on the answer of the previous query.

## Input format

- First line: n and q.
- n - 1 lines: Three space-separated integers u,v,w that represent state u and state v share border whose strength value is w.
- Next line: n space-separated integers where the i-th integer is R[i].
- q lines: Three space-separated integers that are defined in the question

## Output format

For each query, print the answer in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/unhappy-nation-33d0e3b8/
