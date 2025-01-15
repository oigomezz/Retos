# [Micro and Sweet Distribution][link]

It's sweet distribution day in Micro's school. He's very happy. All the students in Micro's class are sitting on chairs which are arranged in a matrix of size N x M i.e. there are N rows of chairs numbered from 1 to N and in each row there are M chairs numbered from 1 to M. Micro is sitting at coordinate (Dx, Dy) (Dyth chair of Dxth row). Teacher gives the box to a student sitting in one of the four corners: (1,1),(1,M) ,(N,1) or (N,M). Students have to take one sweet from the box and pass the box to the next student (student sitting to left, right, front or back). For a student sitting at coordinate (x,y), he'll follow the following priority order:

1. If there is a student in the Right who has not received sweet, then pass it right (x, y+1).
2. If there is a student in the Left who has not received sweet, then pass it left (x, y-1).
3. If there is a student in the Front who has not received sweet, then pass it front (x-1,y).
4. If there is a student in the Back who has not received sweet, then pass it back (x+1,y).
5. Shout Over, meaning that all students have received sweets.

Now, Micro is curious to find out the direction in which he'll have to pass the sweet box. Since there are a lot of students in Micro's class, it will take long for the box to reach him, and you know Micro, he just can't wait. So he asks you to find out the direction in which he'll have to pass the box, or will he have to shout Over.

## Input format

- First line consists of a single integer, T, denoting the number of test cases. Each test case consists of three lines.
  - First line of each test consists of two space separated integer denoting N and M.
  - Second line of each test case consists of two space separated integers Sx and Sy, denoting the coordinate of the corner from which sweet distribution starts.
  - Third line of each test case consists of two space separated integers denoting Dx and Dy, coordinates of Micro.

## Output format

For each test case, print "Left", "Right", "Front", "Back", "Over", depending on whether Micro will pass the box to student in left, right, front or back, or if he'll shout over.

[link]: https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/micro-and-sweet-distribution/
