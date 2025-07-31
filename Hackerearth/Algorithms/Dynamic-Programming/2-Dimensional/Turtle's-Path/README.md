# [Turtle's Path][link]

To be good at problem solving, Monk thinks that Graphs are a topic one can definitely not skip. They have a variety of applications in Networks, flows , Routing and so on.

He has prepared some really interesting problems based on the same for talented programmers like you. He really adores his friends, and has chosen one of this close friends Mona as the main character for this task. So, this is how it goes :

You've got a table of size N\*M containing positive integers. We'll consider the table rows numbered from top to bottom 1 through N, and the columns numbered from left to right 1 through M. Then we'll denote the cell in row x and column y as (x, y).

Initially cell (1, 1) contains one turtle named Mona. Mona wants to get to cell (N, M). Some cells of the table have obstacles. A cell is considered to be containing an obstacle if value of the cell is a NON-PRIME NUMBER. That means that Mona can only move through PRIME Numbers. It is guaranteed that upper left corner (1,1) contains a prime number.

Mona can go from cell (x, y) to one of three cells (x + 1, y ), ( x , y + 1 ) and ( x + 1, y + 1 ) only if the required cell doesn't contain an obstacle. Help him find the number of ways in which it can go from cell (1, 1) to cell (N, M).

In addition, you need to print the lexicographical largest path to reach cell (N,M).

## Input format

- The first line contains two space separated integers, N (number of rows) and M (number of columns).
- Then N lines follow, each containing M space separated integers.

## Output format

In the first line, print the total number of possible ways to reach (N,M) from (1,1). Since this number may be too large, print the answer modulo 10⁹ + 7.

Print the cell indexes (space separated) of each step of his lexicographically largest path in a new line .

If no path exists, only print 0 in first line.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/turtles-path-4/
