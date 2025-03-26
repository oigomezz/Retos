# [Student Arrangement][link]

There is a classroom which has M rows of benches in it. Also, N students will arrive one-by-one and take a seat.

Every student has a preferred row number(rows are numbered 1 to M and all rows have a maximum capacity K). Now, the students come one by one starting from 1 to N and follow these rules for seating arrangements:

- Every student will sit in his/her preferred row(if the row is not full).
- If the preferred row is fully occupied, the student will sit in the next vacant row. (Next row for N will be 1)
- If all the seats are occupied, the student will not be able to sit anywhere.

Monk wants to know the total number of students who didn't get to sit in their preferred row. (This includes the students that did not get a seat at all)

## Input format

- First line contains 3 integers N, M and K. N - Number of students and M - Number of rows and K - maximum capacity of a row.
- Next line contains N space seperated integers Ai. Ai - preferred row of i-th student.

## Output format

Output the total number of students who didn't get to sit in their preferred row.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/student-arrangement-6/
