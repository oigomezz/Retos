# [Don't Jump][link]

Chandu and Kundu are bored of dramatic games around. As they are very good friends and scholars they decided to discover a new game.

In total they had N number of marbles with value inscribed on each of them from 1 to N.
Chandu being from royal family has a treasure box. He emptied the box for the game to proceed.

The game rule involved following operations :

- Operation C : Chandu places a marble in the box. Each different marble can move inside the box only once.
- Operation K : Kundu removes last entered marble from the box and notes down it's value on a chart.

They were deciding further rules when a third person Mr. Chirp comes as a spoiler of the game. Chirp gives them a number N which is the maximum value inscribed among all marbles, and a sequence P. P can possibly be empty. In that case, in input an empty line would be there.

Also, he added following restriction :

- Kundu can perform operation K to take out a marble M only when all the marbles from values 1 to M-1 have went in the box before.

Mr. Chirp kept on chirping and told Chandu and Kundu to generate the sequence of C's and K's for the chart to get filled by pattern P.

Now, you have to help these kids before they jump out of their window in frustration.

## Input format

- First line contains a number N. Next line contains a pattern P(possibly empty).

Read till end of file.

**Note:** Maximum input cases in a file doesn't exceed 2\*10⁴.

## Output format

For each case output on a separate line the minimum length pattern of C's and K's. Print -1 if it's not possible to generate the pattern using the given operations.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/dont-jump/
