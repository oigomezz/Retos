# [Students and their arrangements][link]

There is a long line of students in the mess. Each student has a different roll number. Whenever a student will come in the mess, he will search for his friend from the end of the line. As soon as he finds a friend, he stands behind him else at the end of the line. You are the mess manager. At any moment you can ask the student, who is standing in front of the queue, to come and take the food and go out of the mess.

There are N operations of one of the following types:

- E x: A student whose roll number is x will stand in line according to the method mentioned above.
- D: You will ask the student, who is standing in front of the line, to come and take the food and go out of the mess. For each of the 2nd type of query, print the roll number of the student, who is standing in front of the line, to come and take the food and go out of the mess.

**Note:** Friendship is associative i.e. if a is a friend of b and b is a friend of c, then a is a friend of c.

## Input format

- The first line contains two space-separated integers, N and M, denoting the number of queries and number of friendships respectively.
- Next M lines contain two space separated integers each, a and b, denoting that a is a friend of b.
- Next N lines contain one of the two types of queries.

## Output format

For each of the 2nd type of query, print the roll number of the student, who is standing in front of the line, to come and take the food and go out of the mess.

[link]: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/little-shino-and-friends-98204bd8/
