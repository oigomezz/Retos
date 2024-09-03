# Fredo is in a Hurry

Fredo lives in a building with N+1 floors and his apartment is at floor N. The floors are numbered from 0 to N, N being the highest floor. Fredo has just come from school and is at floor 0. His favourite anime is about to start and he wants to reach his apartment as soon as possible.
He can either use staircase or elevator or a combination of both (use staircase for x floors and cover rest floors by elevator) to reach his apartment.

- If he uses staircase, he takes f amount of time to reach floor f from floor f-1.
- Elevator takes 1 unit time to go from any floor to it's neighbouring floors.

The elevator currently is coming down from floor N .The elevator stops at the floor where the elevator button is pressed .From this floor, the elevator goes to floor N .
Tell him what is the minimum time he needs to reach floor N from floor 0.

Assumptions: Only Fredo uses the elevator during that period of time. Fredo will press the elevator button atmost once. If Fredo presses the elevator button at floor x, then the elevator needs to be at a floor >= x.

## Input format

- The first line consists of an integer T denoting the number of test cases.
- The only line of each test consists of an integer N denoting the number of floors.

## Output format

For each test case, print the minimum time Fredo needs to reach floor N from floor 0 in a separate line.
