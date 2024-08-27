# Roy and Cipher Disk

Roy's friends has been spying on his text messages, so Roy thought of an algorithm to encrypt text messages.

Encryption Algorithm is as follows:
We say message to be encrypted as Plain Text and encrypted form of message as Cipher.
Plain Text consists of lower case alphabets only.
Consider the Cipher Disk as shown in figure.

Initially, we start with 0 (zero). For each character in Plain Text, we move either clockwise or anti-clockwise on the disk depending on which way is closest from where we are currently standing.
If both clockwise and anti-clockwise distances are equal, we give priority to clockwise movement.
Clockwise movements are represented using positive numbers while Anti-clockwise movements are represented as negative numbers.

Roy needs your help in implementing this algorithm. Given a Plain Text message, your task is to encrypt it using above algorithm and print the Cipher Text.

## Input format

- First line contains integer T - number of test cases.
- Each of next T lines contains a string representing Plain Text message.

## Output format

- For each test case, print the encrypted form of given string in new line.
- Each line should consist of space separated integers in the range [-12,13].
