# [Monk's School][link]

Today is the 25th anniversary of Berland International School in Berland. On this auspicious Occasion, our friend Monk has been given the responsibility of preparing the Inventory for his school.

There are exactly N teachers and M students in the school. Each of these teachers teaches arbitary number of students. However, each student is taught by exactly one teacher.

Monk has been given the task of finding out for each teacher the Students he/she teaches. For each student Monk has been given the Student's Name and Age. However , Monk is too busy , So he has assigned this task to us.

We need to print the name of the Teacher and the Name and age of the students that he/she teaches.

However, there is a catch here. We need to print the list of students of each Teacher in Lexicographical order of their names . That is list of the teacher with lexicographically smaller name will appear before other teachers with lexicographically greater names.

In Addition , The students appearing in a particular teachers list should appear in Increasing order of their Age.

## Input format

- The first line contains two integers N and M denoting the number of Teachers and number of Students respectively.
- Each of the next N lines contain a single string denoting a Teachers name.It is guaranteed that each teachers name shall be unique.
- The next M lines contain 2 Strings and an Integer, denoting the Teachers name, a Student's name being taught by that Teacher and that Student's Age. It is guaranteed that each Student's name shall be unique and shall appear only once in the Input.

## Output format

Print N + M lines. Print the teachers name first and then the name and age of each student taught by this teacher. The list of each teacher should appear in order of their lexicographical rank in comparision to all other teachers. For example the list of the teacher with lexicographically smallest name should appear first, then the list of the teacher with the 2nd smallest lexicographical name and so on. The students in a particular teachers list should appear in the output in Increasing order of their Age.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/monks-school-4/
