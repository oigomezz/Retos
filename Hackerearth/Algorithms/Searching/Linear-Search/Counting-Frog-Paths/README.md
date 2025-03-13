# [Counting Frog Paths][link]

There is a frog initially placed at the origin of the coordinate plane. In exactly 1 second, the frog can either move up 1 unit, move right 1 unit, or stay still. In other words, from position (x,y), the frog can spend 1 second to move to:

- (x + 1, y)
- (x, y + 1)
- (x, y)

After T seconds, a villager who sees the frog reports that the frog lies on or inside a square of side-length s with coordinates (X,Y), (X+s, Y), (X, Y+s), (X+s, Y+s). Calculate how many points with integer coordinates on or inside this square could be the frog's position after exactly T seconds.

## Input format

- The first and only line of input contains four space-separated integers: X, Y, s, and T.

## Output format

Print the number of points with integer coordinates that could be the frog's position after T seconds.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/counting-frog-paths-1abd84d5/
