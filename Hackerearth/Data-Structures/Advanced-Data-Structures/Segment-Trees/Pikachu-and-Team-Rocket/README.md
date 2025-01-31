# [Pikachu and Team Rocket][link]

Team Rocket is back with N of their Pokemon to trouble Pikachu. The Team Rocket's Pokemon are numbered from 1 to N and the i-th pokemon has health equal to ai.

Pikachu has to battle multiple Pokemon simultaneously. In a single battle, Team Rocket will make Pikachu fight against all the Pokemon in the range [l,r]. Pikachu can defeat a Pokemon if his attack value is atleast the Pokemon's health. So, he wants to know the minimum attack he must have to defeat all Pokemon in the range.

However, this time, Team Rocket is stronger than ever. They have designed a technology to modify their Pokemon's health as either of two ways:

- Type 1: They choose some k (1 <= k <= N), and then health changes as ai = ai+1 (k <= i < N) and aN = ak.
- Type 2: They choose some k ( 1 <= k <= N ), and then health changes as ai = ai-1 (1 < i <= K) and a1 = ak.

Note that, all health changes occur simultaneously.

There will be Q events. Each event will be either a battle, or some modification of Pokemon's health by Team Rocket.

For each battle, help Pikachu by finding the minimum attack value he must have to win against all Pokemon in the range.

## Input format

- First line contains two space separated integers, N and Q.
- Second line contains initial health values of N Pokemon.
- Next Q lines contain one event each:
  - If the event is a battle, the line contains 1 l r where [l,r] is the range of Pokemon.
  - If the event is modification of type p (1<= p <= 2), the line contains 2 p k where k is the index chosen by Team Rocket.

## Output format

Output one line each for a battling event, containing the minimum attack value required to defeat all Pokemon in the range.

[link]: https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/pikachu-vs-team-rocket-56b518ee/
