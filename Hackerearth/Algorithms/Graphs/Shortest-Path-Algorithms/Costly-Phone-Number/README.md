# [Costly Phone Number][link]

A cell phone company is trying out its new model of cell phone. Here's how its structure is:

The keypad has 11 buttons corresponding to digits from 0 to 9 and one additional button called Add. After pressing any button from 0 to 9, the corresponding digit appears on the screen. The Add button replaces the last two digits appearing on the screen with their sum taken modulo 10. (See sample test for more clarity). If there are less than two digits currently on the screen, pressing Add does nothing.

Each button has a non-negative cost of pressing associated with it. The cost of pressing Add button is always 0. Given the cost of pressing each button and the target phone number, find the minimum cost of feeding that number into the phone screen using a sequence of button presses.

## Input format

- The first line of input file consists of an integer T, which indicates the number of test cases.
- Then the description of T test cases follow. Each test case is described by 3 lines.
  - The first of them contains 10 space separated integers, denoting the cost of pressing buttons from 0 to 9.
  - The second line contains the length of the target phone number.
  - The third line contains the target phone number S itself.

## Output format

Print the minimum cost of feeding the phone screen with the target number for each test case in a separate line.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/costly-phone-number-december-easy-easy-medium/
