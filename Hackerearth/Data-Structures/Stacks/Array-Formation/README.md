# [Array Formation][link]

You are given an array A of n integers. You have to make a queue and stack of the given integers. Queue should contain only prime numbers and stack should contain only composite numbers. All numbers in the array will be >1.

The rule to form the stack and queue is that you should be able to generate the array using the pop and dequeue operations.

**Note:** Please read this explanation carefully

Let the array A contains 5 integers : 7 , 21 , 18 , 3 , 12 then the content of queue and stack will be :

    Queue : 7 , 3
    Stack : 12 , 18 , 21

Now if you follow the rules of stack and queue then you see that you can generate the array using the pop operations of stack and dequeue operation of queue as follows :

    dequeue from queue : 7
    pop from stack : 7 , 21
    pop from stack : 7 , 21 , 18
    dequeue from queue : 7 , 21 , 18 , 3
    pop from stack : 7 , 21 , 18 , 3 , 12

Thus for every array A you have to print the contents of queue in the first line and contents of stack in the second line.

## Input format

- First line contains an integer n as input denoting total numbers of integers in the array.
- Next line contains n space separated integers denoting the elements of array A.

## Output format

In the first line print the contents of queue and in second line print the contents of the stack.

[link]: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/circular-list-8e1319c9/
