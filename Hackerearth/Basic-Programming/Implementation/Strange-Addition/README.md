# [Strange Addition][link]

HackerMan has a message that he has coded in form of digits, which means that the message contains only numbers and nothing else. He is fearful that the enemy may get their hands on the secret message and may decode it. HackerMan already knows the message by heart and he can simply destroy it.

But he wants to keep it incase its needed in a worse situation. He wants to further encode the message in such a format which is not completely reversible. This way if enemies gets hold of the message they will not be completely able to decode the message.

Since the message consists only of number he decides to flip the numbers. The first digit becomes last and vice versa. For example, if there is 3769 in the code, it becomes 9673 now. All the leading zeros are omitted e.g. 15900 gives 951. So this way the encoding can not completely be deciphered and has some loss of information.

HackerMan is further thinking of complicating the process and he needs your help. He decides to add the two flipped numbers and print the result in the encoded (flipped) form. There is one problem in this method though. For example, 134 could be 431, 4310 or 43100 before reversing. Hence the method ensures that no zeros were lost, that is it can be assumed that the original number was 431.

## Input format

The input consists of T test cases. The first line of the input contains only positive integer T. Then follow the cases. Each case consists of exactly one line with two positive integers separated by space. These are the flipped numbers you are to add.

## Output format

For each case, print exactly one line containing only one integer - the flipped sum of two flipped numbers.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/the-reversed-numbers/
