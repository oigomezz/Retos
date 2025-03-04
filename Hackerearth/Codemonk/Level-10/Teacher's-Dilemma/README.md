# Teacher's Dilemma

Monk is having a hard time teaching the 2nd standard students. He wants to divide the students into small groups so that he can conduct some fun-filled activities for them. But students also want their friends in the same group. So, if student A is a friend of student B, and student B is a friend of student C, then the students A,B and C must be in the same group, otherwise they will start crying. After dividing the students, he will choose a leader from each group who will lead their respective groups. Now he wants to know the number of ways he can choose the group leaders from all the groups. Print this answer modulo 10⁹ + 7.

**Note:** Two ways A and B will be considered different if at least 1 person is a leader in group A, and is not a leader in group B, or vice-versa.

## Input format

- The first line consists of two integers N and M denoting the number of students and the number of relationships respectively.
- The next M lines consists of two integers u and v denoting that student u and student v are friends. u and v can never be equal and relationships are not repeated.

## Output format

Print the answer modulo 10⁹ + 7 in a single line.
