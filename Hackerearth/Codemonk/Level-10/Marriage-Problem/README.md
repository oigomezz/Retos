# Marriage Problem

Monk has recently created a matrimonial site. X men and Y women registered there. As Monk has access to everyone's Facebook profile, he can see whether a person is a friend of another person or not. He doesn't want any two people who are in a single group to get married together. So, first we have q1 relationships among men. Then, we have q2 relationships among women. Finally we have q3 relationships among men and women. Read the input format for more clarity. Now, Monk wants to calculate the total number of unique marriages he can set between men and women provided the conditions are followed.

**Note:** Two person are said to be in a group if they are friends directly or connected through a chain of mutual friends.

## Input format

- The first line consists of X and Y.
- Next line consists of variable q1.
- The next q1 lines will have two integers of the form A B where A and B are both men and are friends on facebook and A != B.
- Next line consists of variable q2.
- The next q2 lines will have two integers of the form A B where A and B are both women and are friends on facebook and A != B.
- Next line consists of variable q3.
- The next q3 lines will have two integers of the form A B where A is a man and B is a woman and they both are friends on facebook.

## Output format

Print in a single line the answer.
