# Naruto - The New Hokage

Naruto was declared as the 7th Hokage because of his great contribution in the 4th Shinobi World War. As soon as he aquires office, he changes the process of ranking of Shinobis. Instead of the Genin (Beginner), Chuunin (Intermediate) and Jounin (Expert), the new ranks are numbers ranging from 1 (lowest) to 10 (highest).

There are a total of N ninjas in the Leaf Village, i-th of which has A[i] amount of chakra (energy). A ninja with rank P would have a strength of A[i]^P.

Naruto has Q pending tasks to perform which can be of one of the following types:

- 1 i K: Update the result of training of the i-th ninja i.e. increase the amount of chakra of the i-th ninja by K.
- 2 L R K: Update the result of training of the ninjas ranging from L to R i.e. increase the amount of chakra of the ninjas ranging from L to R by K.
- 3 L R P: Calculate the total strength of the ninjas ranging from L to R provided that each of these ninjas have rank P for sending them to a mission assigned to the Leaf Village. As the value can be very large, calculate it modulo 10⁹ + 7.

## Input format

- The first line of input contains a single integer T denoting the number of test cases.
- The first line of each test case contains a single integer N denoting the number of ninjas in the Leaf Village.
- The next line contains N space separated integers. i-th integer denotes the amount of chakra Ai in the i-th ninja.
- The third line contains a single integer Q denoting the number of pending tasks that Naruto has.
- This is followed by Q lines each containing the description of a task that Naruto has to perform.

## Output format

The output should consist of the answer of all the queries of the 3rd type printed on a new line.
