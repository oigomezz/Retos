# Pikachu vs Team Meowstic and Helping Hand

All the N Meowstic stand in a straight line numbered from 1 to N. Before every round of battle, they simultaneously use a move, called Helping Hand. It changes the attacking power of Team Meowstic as follows:

- The attacking power of first Meowstic remains a1.
- The attacking power of remaining Meowstic changes as ai = ai | ai-1 where 2 <= i <= N and A | B represents the bitwise OR of A and B.

For example, if the current attacking powers are [2,1,4,6,3], after using the Helping Hand, the powers change to [2,1|2,4|1,6|4,3|6], or [2,3,5,6,7].

Help Pikachu by finding the attacking powers of all Meowstic when he fights each of them for the last time, that is, for the Kth round.

Note that, the influence of Helping Hand remains forever, and attacking powers DO NOT revert back after any round.

## Input format

- First line contains two space separated integers, N and K.
- Second line contains N space separated integers, the ith of which is ai.

## Output format

Output a single line containing N integers, the ith of which is ai after the last round.
