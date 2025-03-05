# Little Monk and Steve Smith

Little Monk knows what a dangerous batsman the captain of Australia, Steven Smith is. The bigger problem is that Monk and his team have no idea about the weakness of Smith. But their coach tells them Smith's trick of scoring runs. His trick is pretty simple: he is going to score maximum runs off bowlers who have minimum balls left to be bowled.

For instance, if there are three bowlers -- with 10, 11, 6 balls left respectively in their quota, then Smith would be able to score maximum runs off bowler number 3, then bowler number 1 and then bowler number 2. Let's say bowler 2 bowls the first ball so he'll also have 10 balls remaining, similar to bowler number 1. Now bowler 2 and bowler 1 are on the same number of balls remaining, any of them can bowl the next delivery. But, Monk as the captain in such a case prefers the bowler with in order of occurrence. So, the next ball will be bowled by bowler 1.

So as the captain of the team, Monk needs to know the order of bowlers so that Smith scores minimum runs possible off the K balls he is going to face!

**Note:** None of the bowlers can get Steven Smith out. Also, they are not allowed to bowl once their number of deliveries left is 0.

## Input format

- The first line contains two integers N and K, which denote the number of bowlers faced by Smith and the total number of balls Smith is going to play.
- The next line contains N space separated integers denoting the quota of each bowler.

## Output format

Print K space separated integers denoting the order of the bowlers chosen by Monk. The bowlers are 1-indexed.
