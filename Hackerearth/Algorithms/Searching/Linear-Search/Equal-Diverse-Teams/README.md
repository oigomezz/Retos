# Equal Diverse Teams

Alice has N students in his class, numbered 1 through N. The i-th student has expertise in a subject numbered A[i].

Alice has to divide the students into two teams. The uniqueness of a team is defined as the number of distinct subjects such that there is atleast one student in the team with expertise in the subject. For example, the uniqueness of a team denoted by A = [1,3,1,4,4] is 3.

Alice wants to distribute the students of the class into two teams such that each student belongs to exactly one team and the uniqueness of each team is exactly K. Will he be able to do so?

## Input format

- The first line of input contains an integer T denoting the number of test cases. The description of each test case is as follows:
  - The first line of each test case contains two integers N and K.
  - The second line of each test case contains N integers A[1], A[2], ..., A[N].

## Output format

For each test case, print YES if Alice is able to make two teams satisfying the given conditions, otherwise print NO.
