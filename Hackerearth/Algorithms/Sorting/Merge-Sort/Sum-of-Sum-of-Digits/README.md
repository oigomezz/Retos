# [Sum of sum of digits][link]

Monk likes math problems very much. His math teacher taught him about sum of digits of a number. He decided to experiment a little with them.

Given a number, he recursively finds the sum of its digits till it becomes a single digit number. He calls this as Digit-Value of a number.

It can be written as :

    sumOfDigits(n):
        if n is a single digit number:
            return n
        else:
            x = sum of the digits of n
            return sumOfDigits(x)

After seeing his interest in this concept, his teacher gave him an interesting problem, that uses the above function defined by him. She gave him an array A of N different numbers. Then she asks him Q queries. In each query, he has to form a set of K numbers from the array and find the sum of Digit-Values of those K numbers. This sum is called the value of that set.

The queries are of the following type :

- 1 K : Monk must output the maximum value of a set of size K, that can be obtained, as described above.
- 2 K : Monk must output the minimum value of a set of size K, that can be obtained, as described above.

Monk needs your help to complete this task.

## Input format

- The first line of input contains two space-separated integers N and Q, denoting the number of numbers in the list given by the teacher and the number of queries, respectively.
- The second line contains N space separated numbers, denoting the array A given by the teacher.
- The next Q lines contain two space separated integers each, first one to define query type(1 or 2) and second is K, the size of the set to be formed.

## Output format

Output contains Q lines. Each of these lines contains an integer that denotes the answer to the i-th query.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/sum-of-sum-of-digits-6/
