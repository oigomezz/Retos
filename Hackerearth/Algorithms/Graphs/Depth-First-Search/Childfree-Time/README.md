# [Childfree Time][link]

The weekend is coming soon and you want to spend some time without worrying about your younger son Tommy. He is 6 years old and likes playing computer games a lot. Knowing that, you have written a special computer game for him.

The game is about exploring labyrinths. You have prepared big dungeons to keep him busy for a long time. More specifically, the dungeons consists of R rooms and P portals between them. The rooms are numbered from 1 to R. The portals are one directional and each of them have assigned a time needed to teleport Tommy from one room to another. In order to prevent Tommy from being scared of losing himself in the dungeons, you designed them in such a way that if a player is in a room A, then there is no possibility to use a sequence of portals from A which will teleport him again to A. In order to make Tommy happy, you created some number of rooms without any outgoing portal. Each such room contains a treasure and the game ends as soon as Tommy is teleported to such a room. For any other room, he will take some time to explore it, and you know that the maximum time that he can spend exploring a single room is 2 time units.

Tommy can start the game in any room he wants and you are interested in the maximum number of time units he can spend exploring the dungeons until he finds any treasure.

## Input format

- In the first line there are two integers R and P denoting the number of rooms and the number of portals between them.
- P lines follow. Each of them consists of 3 integers r1, r2, and t. Where r1 and r2 denote respectively the starting and the ending room of a single portal in the dungeons, while t denotes the time needed to travel through this portal.

## Output format

Output exactly one integer denoting the maximum number of time units that Tommy can spend in the game.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/childfree-time-1/
