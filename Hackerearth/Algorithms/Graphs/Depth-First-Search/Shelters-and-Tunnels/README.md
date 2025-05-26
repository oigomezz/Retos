# [Shelters and Tunnels][link]

You are playing a game of shelters with your friends. You and your friends build n shelters and number them from 1 to n. You also dig n-1 tunnels to connect the shelters so that your friends can reach any shelter from other shelters.

The rules of the game are as follows:

It’s a one-player game. A person starts from a shelter v and writes the number of shelter in his notebook. The player ties a rope to one of the shelter’s jamb and connects the other side of the rope to himself or herself. If there is a neighboring shelter that the player has not seen it yet, then he or she would have to select one of them (if there is more than 1) and go to that shelter and writes the number of the shelter in his notebook. The player must continue doing this as many times as he or she can. If there is no neighboring shelter that the player has not seen, then he or she would have to go back to the shelter which is adjacent to the current shelter and also the rope passes through that shelter. The game ends when the number of all shelters are written in the notebook (the algorithm that is applied here is similar to the DFS algorithm).

You must be able to create the most different sequence of numbers in the notebook. The shelters that create the most different sequence by starting the game from them, are called good shelters. Your task is to determine the number of good shelters and print them in increasing order.

## Input format

- First line: Contains a single integer n that represents the number of shelters.
- Each of the next n-1 lines: Contains two integers x and y, denoting a tunnel that connects shelter with number x and shelter with number y.

## Output format

The format of the output is as follows:

- In the first line, print the number of good shelters.
- In the second line, print the good shelter’s numbers in the increasing order.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/kavirioo-back-up-754d2621/
