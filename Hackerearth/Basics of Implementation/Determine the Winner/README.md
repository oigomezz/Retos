# Determine the Winner

Assume there are two programmers with their hacker names as "Flash" and "Cisco". They both took part in a contest. The rules of the contest are:

1. There will be 4 questions to solve, P, Q, R and S.
2. Initial score (before the start of the contest) of the 4 problems is s_p, s_q, s_r and s_s.
3. After each minutes, the score of the questions, P, Q, R and S, will decrease by d_p, d_q, d_r and d_s respectively. The score cannot decrease below half (integer division) of the initial score for each question i.e. at a particular time, the score of the problems will be maximum of half of the initial score and the decreased score.

Flash submitted the solutions of the questions at time f_p, f_q, f_r and f_s. Cisco submitted the solutions of the questions at time c_p, c_q, c_r and c_s. Your task is to find winner of contest. The winner is the one who has more score. If the score of both the programmers is same, then winner will be the one who took less time to solve all the questions. If both the problems have same score and took same time to solve the questions, then print Tie.

**NOTE:** All the times mentioned above are in minutes. Time taken to solve all the questions is the time at which programmers submitted the last solution.

## Input format

- First line of input contains an integer T, denoting number of test cases.
- First line of each test case contains 4 space separated integers s_p, s_q, s_r, s_s denoting the initial scores for each problems.
- Second line of each test case contains 4 space separated integers d_p, d_q, d_r, d_s denoting the decrease in each problem's score after each minute.
- Third line of each test case contains 4 space separated integers f_p, f_q, f_r, f_s denoting the time when Flash submitted his solutions.
- Fourth line of each test case contains 4 space separated integers c_p, c_q, c_r, c_s denoting the time when Cisco submitted his solutions.

## Output format

Print the winner of the competition **Flash** or **Cisco**. If both the problems have same score and took same time to solve the questions, then print **Tie**.
