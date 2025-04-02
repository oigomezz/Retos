# [AltF4 and the beetles][link]

It is a nice winter Sunday morning and AltF4, our hero, decides to play a new video game. The game is called Appearism. There are a total of N beetles in the game that are initially peeping out of the grooves to look for a chance to tease you.Each one appears out of their groves at an absolute time Pi, tease AltF4 for a time duration and then go back to their groves and sleep forever at time Qi.

AltF4 has just got one shot of the nuclear weapon that ha can use to destroy all the beetles. Being very clever, he has noted down the (Pi, Qi) for each of the beetles. He also observed that the beetles are hurt by a amount A when they are looking for a chance to tease you in the groove (i.e. when time is < Pi), by B when they are out of their grooves teasing you (between Pi, Qi) and by C when they are back into the grooves and sleeping forever (when time is > Qi). Obviously B is always greater than both A and C. AltF4 being poor in math and computing asks you for favor.

## Input format

- The first line contains the number of times AltF4 plays the game T.
- Then the description of T games follow:
  - The first line contains four space separated integers N A B C.
  - Then N lines follow with two space separated integers P Q, the recorded value of their hideouts. Each Q will always be ≥ corresponding P

## Output format

For each test game, you are to print one number in a line, the maximum destruction that AltF4 can achieve. Remember that he may use the nuclear gun only at one instant of time.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/altf4-and-the-beetles/
