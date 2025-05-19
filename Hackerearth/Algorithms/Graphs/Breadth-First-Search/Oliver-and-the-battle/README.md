# [Oliver and the battle][link]

Colonel Oliver and his battalion were in midst of a battle against an extraterrestrial species Zomni. The Colonel has to win the battle at any cost to save all of humanity. He was short of soldiers, however, he had a very powerful weapon bazooka which could be used only once during the war.

The Zomni army was divided into small troops scattered at different locations (which can be contained in a N x M battle ground). The bazooka, once launched on some troop is capable of killing all the Zomnis of that troop at a time but cannot harm any Zomni soldier in other troops.

The war is coming to an end and the Colonel is about to lose. He has only one bazooka but something he knows for sure is that if he is able to kill the maximum possible soldiers with this bazooka, he and his soldiers definitely have a chance of winning the battle.

So, the Colonel seeks your help in finding out the maximum number of Zomnis he can kill in one strike of the bazooka and also the total number of Zomni troops gathered against them so that he can divide his battalion efficiently (the troop killed by the bazooka should also be included).

Two Zomni soldiers belong to the same troop if they are at adjacent positions in the battle ground. Therefore, any soldier who is not at some boundary of the battle ground can have a maximum of 8 adjacent soldiers.

## Input format

- First line contains single integer T, the number of test cases.
- First line of each test case contains two space separated integers N and M (size of the battle ground).
- Followed by N lines containing M integers 0 or 1 where 0 means an empty space and 1 means a Zomni soldier.

## Output format

For every test case, output two space separated integers X and Y where X is the number of Zomni troops and Y is the maximum number of Zomnis that can be killed by a single strike of the bazooka.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/oliver-and-the-battle-1/
