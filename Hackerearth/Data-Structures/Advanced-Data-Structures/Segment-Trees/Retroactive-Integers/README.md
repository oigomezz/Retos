# [Retroactive Integers][link]

You're maintaining 20 variables: a,b,c,...,r,s,t. At any moment of time value of any variable is integer between 0 and 10⁹ + 6, inclusive. All arithmetic operations with variables are modulo 10⁹ + 7. Initially (at moment 0) all variables are set to 0. At some moments of time, you get queries. Queries have 5 different types:

1. "? x" print value of variable x.
2. "= x y" write value of variable y to variable x.
3. "! x c" set variable x to c.
4. "+ x c" add c to variable x.
5. "\* x c" multiply variable x by c.

Also with each query you are given a positive integer --- time when you need to apply this query to variables. Times can go in arbitrary order. See sample for further clarification.

## Input format

- First line contain one integer q --- number of queries.
- Next q lines contains queries. i-th query starts with integer t[i] --- time this query should be made at.
- Then one of 5 query goes in format, described in the statement.

## Output format

For each query of the first time print the corresponding value.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/retroactive-integers/
