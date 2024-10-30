# Shooting Range

Three friends Snow Gnome, Small Boy and Xephy were having fun in the biggest park in Lalalandia, when suddenly they saw the shooting range with prizes! As always, Small Boy asked for the biggest prize, and Snow Gnome said he would get it.

The shooting range consists of N towers each denoted by K[i] lines (1 <= i <= N). Towers are described by blocks from the bottom to the top. Each block consists of Aij cubes and the shooter gets Bij coins for taking one cube in this block for 1 <= j <= K[i].

The shooter gets Q shots. He shoots the bullets in straight line on height C[l]. After the bullet shoots the cube, it gets destroyed, and all cubes above it move down. Note that bullet, even after penetrating one tower, continues to go through and never goes down.

Xephy now wants to know how many points for each shot Snow Gnome got. Can you help him with that?

## Input format

- First line contains single integer N - the number of towers.
- Next N lines describe the tower i (1 <= i <= N) - each contains single integer K[i]. Next K[i] lines contain the numbers Aij and Bij for 1 <= j <= K[i] - the number of cubes and the coins for shooting one cube from this block, respectively.
- Next line contains Q - the number of Snow Gnome's shots. The Q lines describe the lth shot (1<= l <= Q) - each containing one integer C[l]- the height of the lth shot.

## Output format

The output should contain Q lines. lth line should contain single integer - points for Snow Gnome's lth shot (1 <= l <= Q).
