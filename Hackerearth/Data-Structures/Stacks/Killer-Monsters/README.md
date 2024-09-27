# Killer Monsters

Given an array monsters denoting strengths of N monsters, we start with an empty battlefield, at each minute i, the ith monster joins the battlefield and kills all monsters whose strength is less than or equal to his strength.

Find the number of monsters alive in the battlefield at end of ith minute for each 0 <= i < N.

## Input format

- First line contains an integer T, the number of test cases.
- First line of each testcase contains an integer N, the number of monsters.
- Second line of each testcase contains N space seperated integers, the strengths of N monsters.

## Output format

For each testcase, output N integers denoting the number of monsters alive after ith minute for each 0 <= i < N.
