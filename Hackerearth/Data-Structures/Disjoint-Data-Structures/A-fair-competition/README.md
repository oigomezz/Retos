# [A fair competition][link]

In competition, N participants are competing against each other for the top two spots. There are M friendly relations between participants. In each friendship relation, you will be given two integers L and R, indicating L and R are friends.

Note

- If A and B are friends, B and C are friends, then A, B, C will have the same friend circle.
- Two combinations are considered different if either first or second ranker is different.
- The same friendship relation can occur multiple times in input, however, L will never be equal to R.

Now, the jury has to decide the winners for the top two spots but he does not want to select both participants from the same friend circle so the competition seems fairer. Find the number of ways in which he can do so.

## Input format

- The first line contains T denoting the number of test cases.
- The first line of each test case contains two space-separated integers N and M denoting the number of participants and the number of friendly relations.
- Next M lines of each test case contain two integers L and R indicating a friendly relation between L and R.

## Output format

For each test case, print a single line denoting the number of ways in which the jury can choose the top two participants.

[link]: https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/fair-competition-0315250e/
