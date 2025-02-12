# [Hacker with Team][link]

Alex has learnt many new concepts in hacking, and created his own team. He has N people (excluding Alex) in his team, where i-th person has individual skill value S[i] where 1 <= i <= N. They are standing in a particular order, where 1-st person being the leftmost person and N-th person being the rightmost person.

Alex has found a special way to evaluate the contribution done by each person in the team. Contribution done by i-th person (C[i]) in the team can be calculated as sum of his skill value and the skill values of his K adjacent team members on the left side, where the value of K will be decided by Alex.

In case, there are not enough members on the left side, contribution will be equal to the sum of his skill value and the skill values of all the team members on the left side.

Alternatively, C[i] = Σ S[j]

Alex can perform 2 types of operations now:

1. He can write a program to calculate the total contribution done by all the team members in the range of l to r (both inclusive), where contribution of each person will be calculated using value of K decided by him.

2. He can ask any person to change his skill value to X.

Being a great hacker, he is busy with other tasks, and needs your help in performing above operations.

## Input format

- First line contains 2 space-separated integers N and Q, where N denotes the number of people in Alex's team and Q denotes the number of operations Alex wants to get completed.
- Second line contains N space-separated integers, where i-th integer denotes the skill value of i-th person in the team.
- In next Q lines, each line contains first integer O, which represents the type of operation.
  1. For O = 0, line will contain 3 more space-separated integers l,r and K. Here Alex wants to know the total contribution done by all team members in the range l to r (both inclusive), where contribution of each person will be calculated using value of K decided by him.
  2. For O = 1, line will contain 2 more space-separated integers i and X where Alex asks i-th person to change his skill value to X.

## Output format

For each operation of the 1-st type, print the required answer in the new line.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/hacker-with-hack-function-03dd9bc0/
