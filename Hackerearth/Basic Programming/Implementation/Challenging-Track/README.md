# Challenging Track

Alice and Bob saw a challenging track which consists of N hurdles of variable heights Hi. Now, Bob challenges Alice to complete this track with a given amount of jump power P.

The rules for completing the challenge are as follows:

1. Each time Alice jumps a hurdle, jump power P of Alice reduces by the height of the hurdle.

2. Every even minute all the remaining hurdles having even heights will decay and their heights reduce by 1 and every odd minute all the remaining hurdles having odd heights will decay and their heights reduce by 1.

Initially, time T = 0 minute. It takes 1 minute for Alice to reach to the next hurdle and the time taken to jump a hurdle can be considered to be negligible. Alice has to complete the challenge starting from the first hurdle to the last hurdle, left to right, sequentially.

If P < 0 at any moment, Alice cannot move further. Find out if Alice can complete the challenge?

## Input format

- The first line of the input contains T, the total number of test cases.
- The second line of the input contains two space-separated integers N and P, the total number of hurdles and the total jump power value.
- The next line contains N space-separated integers Hi, the heights of each hurdle.

## Output format

For each test case, if it is possible for Alice to complete the challenge, print Yes and the remaining value of jump power P or No if it is not possible.
