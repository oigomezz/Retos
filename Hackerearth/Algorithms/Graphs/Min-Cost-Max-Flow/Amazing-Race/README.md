# [Amazing Race][link]

It is the final leg of the most famous amazing race. The top 'n' competitors have made it to the final. The final race has just begun. The race has 'm' checkpoints. Each team can reach any of the 'm' checkpoint but after a team reaches a particular checkpoint that checkpoint gets closed and is not open to any other team. The race ends when 'k' teams finish the race. Each team travel at a constant speed throughout the race which might be different for different teams. Given the coordinates of n teams and m checkpoints and speed of individual team return the value of minimum time needed to end the race.

The time required for a team at coordinate (p,q) with speed 's' to reach a checkpoint at coordinate (x,y) is given by:

t = ceil( ((p-x)^2 + (q-y)^2) / s^2 ). For example if distance is 5 units and speed is 2 units then required time = ceil(25/4) = 7.

## Input format

- The first line contains 3 integers n, m and k denoting the total number of competitors, total number of checkpoints and the minimum number of teams that must complete the race in order to end the race.
- This is followed by n lines each indicating the coordinates of n teams.
- This is followed by m lines each indicating the coordinates of m checkpoints.
- This is followed by n integers each denoting the speed of the ith team

## Output format

Print the minimum time required to end the race.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/practice-problems/algorithm/amazing-race-3/
