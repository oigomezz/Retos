# [Counting In Byteland][link]

For once, lets assume Byteland to be a 3 dimensional space of size N X N X N. The Lolympics Committee has decided that every contingent representing a country will stay in a hotel at a particular coordinate denoted by its x-axis, y-axis and z-axis. Now, the Players Welfare Association(PWA) has to answer some queries as well as give accommodation to the Lolympic players. There will be Q number of queries which can be of two types:

1. 1 x y z val - A contingent consisting of val number of players have been alloted a hotel in the coordinate (x,y,z).
2. 2 x y z X Y Z- Calculate the total number of players who are not residing in the coordinates ranging from (x <= xi <= X, y <= yi <= Y, z <= zi <= Z)

## Input format

- The first line consists of two numbers N and Q.
- Next Q lines consists of queries of the two forms mentioned above.

## Output format

Print the answer for query 2 in a single line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/counting-in-byteland/
