# [Terminators][link]

War is raging between Humans and Cyberdyne Systems. Our intel has shown that Cyberdyne has prepared a large army of terminators to exterminate humans from the face of Earth. We need to prepare for battle!

We sent some spies to the Terminator camp to gather more information about their tactics. Our spies observed the following:

1. There are a total of n terminators in the camp. They are numbered from 1 to n. All terminators have a unique strength level.
2. They are divided into groups. Each group has a certain number of terminators in it. The size of each group may be different.
3. Every day the terminators stand in a queue for inspection. The spies observed that the terminators stood in such a way that a terminator never stands ahead of a stronger terminator of his group. A terminator may stand ahead of a stronger terminator of a different group.

The spies observed the camp for two days. They noted down the position of each terminator in the queue for each day. The supreme Commander of the Human Army has appointed you. Your job is to tell the maximum possible number of terminators in one group.

## Input format

- The first line of the input contains the number of test cases, t.
- The first line of each test case has the n, the number of terminators.
- N lines follow. The i-th line has two integers, p1 and p2. P1 is the position of the i-th terminator in the inspection line as observed on the first day. P2 is the position of the i-th terminator in the inspection line as observed on the second day.

## Output format

For each test case, output a single line containing the maximum number of terminators that may belong to the same group.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/terminators/
