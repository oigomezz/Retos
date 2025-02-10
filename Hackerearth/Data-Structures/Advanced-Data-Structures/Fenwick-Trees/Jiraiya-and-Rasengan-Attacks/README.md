# Jiraiya and Rasengan Attacks

Naruto has started training from Jiraiya to develop the most powerful Rasengan attack. Jiraiya as always uses weird training exercises.

Jiraiya has brought a permutation P of 1,2,...,N integers. He tells Naruto to sort the permutation using minimum number of Rasengan attacks. In one Rasengan attack Naruto can choose any pair of consecutive elements of the permutation and swap it.

To make the task a little difficult, he chooses a subsegment of the permutation uniformly at random P[L], P[L+1], ..., P[R] (L ≤ R) and reverses it to make P[1], P[2], ..., P[L-1], P[L], P[L+1], ..., P[R], P[R+1], ..., P[N]. Now he asks Naruto to tell the expected number of Rasengan attacks he need to sort the permutation.

## Input format

- The first line contains the integer N.
- The next line contains N integers denoting the permutation P.

## Output format

Print (A \* B⁻¹) mod 10⁹ + 7 where A / B is the Expected value of number of Rasengan attacks he need to sort P (expressed as an irreducible fraction)
