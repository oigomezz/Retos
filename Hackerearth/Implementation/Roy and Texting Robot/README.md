# Roy and Texting Robot

Roy frequently needs to use his old Nokia cell phone for texting whose keypad looks exactly as shown below.

You may be already familiar with the working of the keypad, however if you're not we shall see a few examples.

To type "b", we need to press "2" twice. To type "?" we need to press "1" thrice. To type "5" we need to press "5" four times. To type "0" we need to press "0" twice.

I hope that it's clear how the keypad is being used.

Now Roy has lot of text messages and they are pretty lengthy. So he devised a mechanical-hand-robot (with only 1 finger) which does the typing job. One drawback of this robot is its typing speed. It takes 1 second for single press of any button. Also it takes 1 second to move from one key to another. Initial position of the hand-robot is at key 1.

So if its supposed to type "hack" it will take 1 second to move from key 1 to key 4 and then 2 seconds to type "h".
Now again 1 second to move from key 4 to key 2 and then 1 second to type "a".
Since "c" is present at the same key as "a" movement time is 0. So it simply takes 3 seconds to type "c".
Finally it moves from key 2 to key 5 in 1 second and then 2 seconds to type "k". So in total it took 1+2+1+1+3+1+2= 11 seconds to type "hack".

## Input format

- First line contains T - number of test cases.
- Each of next T lines contain a string S - the message Roy needs to send.
- Each string is terminated by a newline escape sequence \n.

## Output format

For each test case output the time taken by the hand-robot to type down the message.
