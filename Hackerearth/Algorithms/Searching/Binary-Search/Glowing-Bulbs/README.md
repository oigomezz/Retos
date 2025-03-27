# [Glowing Bulbs][link]

There is an infinite series of bulbs indexed from 1. And there are 40 switches indexed from 1 to 40. Switch with index x is connected to the bulbs with indexes that are multiple of x. i.e switch 2 is connected to bulb 4, 6, 8 ....

You can easily observe that some bulbs are connected to multiple switches and some are not connected to any switch.

Chotu is playing with these switches, he wants to know the Kth glowing bulb from the start if certain switches are in ON state. If any of the switch is ON, connected to any bulb then bulb starts glowing. But chotu has special fond of prime numbers so he only puts prime indexed switches ON.

## Input format

- First line contains number of test cases (T).
- Each test case contains two lines
  - First line contains a string S of length 40 containing 0s and 1s that represents the state of bulbs. 1 is ON , 0 is OFF.
  - Second line contains one integer k. Atleast One switch is in ON condition.

## Output format

Output one integer per test case representing k-th glowing bulb.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/glowing-bulbs/
