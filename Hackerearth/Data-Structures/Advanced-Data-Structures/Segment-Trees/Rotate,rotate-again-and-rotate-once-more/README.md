# [Rotate, rotate again and rotate once more][link]

Mr Lavit is teacher for physical education at a school. Today he is in bad mood, so he is taking it out on the students of his class. There are N students in his class. Lets mark the students from 1,2,.. up to N. They are standing in a line.Initially, all the students are facing towards EAST. Now he makes them sweat in sun.

He gives 3 types of orders to his class

- Order 1: C L R K where C is character 'C', stands for clockwise, L is a number 1 <= L <= N, R is a number L <= R <= N, K is a number denoting number of steps to rotate. This type of order means students in positions [L,R] has to rotate K steps clockwise.

- Order 2: A L R K where A is character 'A', stands for anti-clockwise, L, R, and K are the same as in previous order. This type of order means students in positions [L,R] has to rotate K steps anti-clockwise.

- Order 3: Q L R where Q is character 'Q', stands for query, L is a number 1 <= L <= N, R is a number L <= R <= N, This type of order is a query where he asks his class the maximum number of students facing in a same direction in [L,R] positions.

If number of students facing in two, or more directions are maximum and equal, output this maximum value.

If students answer wrong or answers very late then he may not let them go easily, so they have asked for your help. Answer these queries on their behalf.

Rotation Explanation:

- Suppose a student is facing EAST, Now if he is ordered to rotate 1 step clockwise then he would turn towards SOUTH, so now he will be facing SOUTH

- He is facing SOUTH, now if he is ordered to rotate 2 step clockwise, then he would turn WEST, then to NORTH. so now he will be facing NORTH

- He is facing NORTH, now if he is ordered to rotate 5 steps anti-clockwise, then he would turn (1) WEST, (2) SOUTH, (3) EAST, (4) NORTH , then (5) WEST so now he would be facing WEST.

      Clockwise direction [ EAST-->SOUTH-->WEST-->NORTH-->EAST ]
      Anti-Clockwise direction [ EAST-->NORTH-->WEST-->SOUTH-->EAST ]

## Input format

- First line of the input contains N, M separated by space, N is the number of students in class, M is the number of orders.
- Now M lines follow, each line contains one of the following three types of order C L R K or, A L R K or, Q L R

## Output format

For every order of type 3, i.e "Q L R" , output the required number in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/rotate-rotate-again-and-rotate-once-more-4/
