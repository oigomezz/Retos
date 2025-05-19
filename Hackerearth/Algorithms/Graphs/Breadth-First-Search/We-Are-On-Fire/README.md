# [We Are On Fire][link]

An intergallactic war is on. Aliens are throwing fire-balls at our planet and this fire is so deadly that whichever nation it hits, it will wipe out not only that nation, but also spreads to any other nation which lies adjacent to it.

Given an NxM map which has N x M cells. Each cell may have a country or else it may be the ocean. Fire cannot penetrate the ocean or go beyond the edges of the map (a wise man managed to bound the corners preventing fire from wrapping around the corners).

You will be given a initial state of the planet represented by an N x M grid consists of 0 or 1 representing ocean and nation respectively. Also there will be Q attacks of the fire-ball. After each query, you are to tell the number of nations still left unburnt.

## Input format

- First line of input contains 3 space separated integers N,M,Q where N x M is the size of the planet. Q is the number of fire-ball attacks.
- N lines follow each with M values of either 0 or 1, denoting whether that particular coordinate is a nation(1) or ocean(0).
- Q lines follow. Each line has a coordinate X,Y where the next fire-ball attack takes place.

## Output format

For each Q, output the number of nations still existing on a single line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/we-are-on-fire/
