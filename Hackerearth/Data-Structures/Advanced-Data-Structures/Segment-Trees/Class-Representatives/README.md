# [Class representatives][link]

John teaches a class of n students. Each student is assigned a unique roll number from 1 to n. He also knows the heights of each student. He needs to select a set of class representatives (a class can have any number of representatives).

A set of students are valid candidates for representatives if the following condition holds:

- There does not exist a pair of students i,j such that roll[i] < roll[j] and height[i] >= height[j].

John wants to select the maximum number of students as class representatives. However, he has a new student that got enrolled whose height is x. In order to increase the number of class representatives, John assigns him a roll number i (from 1 to n+1) randomly and then increases the roll numbers of all those students by 1 whose roll number is >= i. If the number of class representatives does not increase after this process, then he repeats the same procedure (he again assigns him a roll number from 1 to n+1 randomly after reverting the roll numbers of all the existing students from 1 to n). Determine the expected number of times John needs to repeat this procedure in order to increase the number of class representatives.

## Input format

- First line: Two integers n (the number of students) and x (the height of the new student).
- Next n lines: Two integers ri and hi denoting the roll number and height of the i-th student. It is guaranteed that no two students have the same roll number.

## Output format

Print the expected number of times John needs to assign the roll number to the new student using the above procedure to increase the number of class representatives. If the expected value is of the form a / b, then print a \* b⁻¹ modulo 10⁹ + 7. If it is not possible to increase the number of class representatives, then print -1.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/the-dumb-classroom-97e11ab7/
