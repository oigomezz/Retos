# [Balanced Buildings][link]

Cat Noku recently picked up construction working as a hobby. He's currently working with a row of buildings and would like to make it beautiful.

There are n buildings in a row. The height of the i-th building is xi.

Cat Noku can modify the buildings by adding or removing floors to change the heights. It costs him P dollars to increase the height of one building by 1, and M dollars to lower the height of one building by 1. Note that the heights of all the buildlings must remain integers (i.e. Cat Noku cannot choose to raise the height of a building by 0.5).

At the end of the day Cat Noku will get a bonus for the number of buildings which are adjacent and have the same height. For each section i, if section i+1 has the same height, Cat Noku will gain a profit of S (of course, it is not possible to get this bonus for the last building in the row). Thus, his net profit can be described by his total profit minus the cost it took him to change the building heights.

Help Cat Noku determine the maximum possible net profit he can gain.

## Input format

- The first line will contain four space separated integers n, S, M, P.
- The second line will contain n space separated integers. The i-th integer in this line will be equal to xi.

## Output format

Print a single integer on its own line, the maximum net profit that Cat Noku can earn.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/balanced-buildings/
