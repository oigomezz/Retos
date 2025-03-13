# [Velocities of balls][link]

There are n balls along a number line, each ball is represented by a point on the line. Ball i moves at velocity vi (vi != 0) along this number line and is initially at point xi.

When two balls collide (occupy the same point along the number line), their velocities switch. For example, if ball i with velocity 2 collides with ball j with velocity -3, ball i will have velocity -3 and ball j will have velocity 2 after the collision.

Given each ball's initial distinct position and velocity, find for each ball i the sum of the floor of the times that ball i collides with another ball. Formally, ball i collides with another ball k times in total at times t1,t2,...,tk.

It is guaranteed that whenever two balls i,j collide, the signs of their velocities will be different (vi \* vj < 0).

## Input format

- The first line of the input contains a single integer t denoting the number of test cases.
- The first line of each test case contains a single integer n denoting the number of balls.
- The second line of each test case contains n integers xi denoting the initial position of ball i.
- The third line of each test case contains n integers vi denoting the velocity of ball i.

## Output format

Print n integers denoting the i-th being the sum of the floors of each time ball i collides with another ball.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/bouncing-balls-b9c19a3d/
