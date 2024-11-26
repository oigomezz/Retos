# Team Up

N children want to play a game, so they need to form teams. Each child has strength. The strength of the i-th children is i. Initially, no team is created, and all children are on their own, so there are N teams in the beginning.

You need to perform Q queries to help them in the team forming task. The query can be of 3 types as follow:

- 1 A B: Combine the team where A belongs with the team where B belongs. If both belong to the same team, nothing needs to be done.
- 2 A: Print the size and the total strength of the team where A belongs.
- 3 A B: Move child A to the team where child B belongs. If both belong to the same team, nothing needs to be done.

For each query of type 2, you need to output two things, the team's size and total strength.

## Input format

- The first line contains a single integer T denoting the number of test cases, then the test case follows.
- The first line of each test case contains two single space-separated integers, N and Q.
- The following Q line contains the query one of any three types.
- It is guaranteed that there will be at least one query of type 2 in each test case.

## Output format

For each test case, output an array that contains the answer for every query of type 2.
