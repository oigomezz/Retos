# [Round Table Killers][link]

There is a round table in which N people are sitting. You can look at the image for their seating arrangement. Initially the person numbered X holds a gun. In addition to it there is a special number K that helps in determining the persons to be killed. The killing starts as follows - Firstly the person numbered X starts and he kills a total of X % K people sitting clockwise of him and he gives gun to the person i who is sitting just next to the last person killed. Now that person also kills the next i % K people and this goes on. If at any instant the total persons that are remaining is not greater than i % K where i is the number of person holding the gun then the person i wins. You can show that sooner or later only one person remains. So your job is to decide which numbered person will win this killing game. X % K is the remainder when X is divided by K

## Input format

First line contains three numbers N , K and X as input.

## Output format

In the output you have to tell the number of the player who will be the winner.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/round-table-killers-b7b93156/
