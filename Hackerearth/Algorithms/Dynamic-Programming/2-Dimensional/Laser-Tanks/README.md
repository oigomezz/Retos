# [Laser Tanks][link]

Several tanks have been arranged in N x N grid with each cell containing exactly one tank. These tanks are laser tanks - they shoot continuous laser beams instead of bullets. Each tank can shoot in two directions - upwards and rightwards, but in only one direction at a time. Tank located in ith row and jth column can shoot in upwards direction with power Vij and in rightwards direction with power Hij. However, if any horizontal laser beam meets vertical laser beam, they creates a big explosion. That's why, you have to assign directions to tanks in such a way that no explosion happens and maximum firepower is achieved. Firepower is defined as total power of all laser beams which have been shot by the tanks.

## Input format

- First line of input will consists of integer N denoting size of the grid.
- Next N lines will contain N integers, jth integer in the ith line will contain Hij.
- Similarly, Next N lines will contain N integers denoting matrix Vij

## Output format

Output the maximum total firepower that can be achieved.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/shooting-tanks-8dcc4adb/
