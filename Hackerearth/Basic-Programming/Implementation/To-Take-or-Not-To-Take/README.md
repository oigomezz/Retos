# [To Take or Not To Take][link]

Pandey needs your help. As you know, he is on the quest to save the princess. After traveling for a number of days, he has finally reached the palace, but one last battle remains to be fought. However he has only one unit of energy left in him. To win the battle, he needs all the energy he can get. So he is searching for the Wizard of GJ.

GJ agrees to help him if he is willing to play his game. GJ will give him B balloons, one at a time. For each balloon, he will ask Pandey if he wants to take the balloon. If Pandey accepts, his energy level will be changed according to the value and type of the balloon. Otherwise, the balloon is lost forever.

GJ is hoping to enjoy seeing Pandey regret his choices after every move because Pandey will only know the current balloon offered to him and will have no knowledge of the following ones. However, unknown to GJ, Pandey's brother Vajpayee had been working undercover as GJ's apprentice and knew in advance the values on each of the balloons and also the order in which he would show them to Pandey. So, Pandey knows all the details, and now he needs you to help him select the balloons so that he can maximize his energy.

Each balloon may be of one of the following types:

- \+ X : Taking this balloon will add X to the current energy of Pandey.
- \- X : Taking this balloon will subtract X from the current energy of Pandey.
- \* X : Taking this balloon will multiply X to the current energy of Pandey.
- / X : Taking this balloon will divide (integer division) the current energy of Pandey by X. To simulate this balloon, you can use a standard division operator in most of programming languages. E.g. 7 / 4 = 1 and (-7) / 4 = -1.
- N : Taking this balloon replaces Pandey's energy by its negated value.

## Input format

- The first line contains T which is the number of test cases.
- The first line of every test case contains an integer B which represents the number of magic balloons offered to Pandey by GJ.
- B lines follow, each containing one of the 5 possible balloon types in the order in which they are shown to Pandey.

## Output format

For each test case, output a line containing the maximum energy Pandey can make with the given balloons offered by GJ. Pandey starts with energy equal to one.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/totakeornottotake/
