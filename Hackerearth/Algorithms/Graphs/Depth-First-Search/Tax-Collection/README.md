# [Tax Collection][link]

You are a CEO of a group of companies (N companies form a rooted tree structure), and the country you live in has a weird tax system. Suppose if a company makes X rs profit then it has to pay Y rs tax, here the Y is the number of prime factors of X. Calculate the total tax paid by all the companies in the group. Company 1 is the parent of all companies.

Tax paid by a company is equal to the tax paid by its direct children and the tax paid on the profits earned by that company.

## Input format

- The first line contains T, the number of test cases.
- The first line of each test case contains N, the number of companies.
- The second line of each test case contains an array profit a1,a2,..., an.
- The next N-1 lines contain two numbers u,v. There is an edge between u and v.

## Output format

Print an array of size N, where Ai is the amount of tax paid by the company i.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/tax-collection-8e1d0a45/
