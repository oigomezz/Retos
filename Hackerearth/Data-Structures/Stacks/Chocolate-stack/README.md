# Chocolate stack

A shop has a stack of chocolate boxes each containing a positive number of chocolates. Initially, the stack is empty. During the next N minutes, either of these two things may happen:

- The box of chocolates on top of the stack gets sold.
- You receive a box of chocolates from the warehouse and put it on top of the stack.

Determine the number of chocolates in the sold box each time he sells a box.

- If C[i] = 0, he sells a box. If C[i] > 0, he receives a box containing C[i] chocolates.
- It is confirmed that he gets a buyer only when he has a non-empty stack.
- The capacity of the stack is infinite.

## Input format

- The first line contains N denoting the number of minutes.
- The second line contains C denoting the array consisting of the box descriptions.

## Output format

Print an array, representing the number of chocolates in the sold box each time you sell a box.
