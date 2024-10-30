# Fibonacci with GCD

Monk is really fond of Recurrence Relations, and he likes to study their characteristics in any possible manner. As you might know, his favorite one among all such recurrences is the famous Fibonacci series. For those of you who haven't,

Fibonacci series is defined as:

- F(N) = F(N-1) + F(N-2), for all N >= 3
- F(1) = 1, F(2) = 1.

Now, in addition to such sequences, Number Theory is a really interesting concept, and Monk loves solving problems of those kinds too. GCD is a nice concept within the scope of this topic, and is defined to be :

The GCD of two numbers is the greatest common divisor of those numbers. Eg: GCD(2,4)=2. Here, he has challenged you to the following task as he feels that this one is amazingly challenging . So, this is how it goes :

You are given N integers, a1,a2,...,an and Q queries. In each query, you are given two integers L and R. For each query, you have to find the value of:

GCD(F(A[L]), F(A[L+1]), F(A[L+2]), ..., F(A[R])) % 10⁹ + 7.

## Input format

- First line : Two integers N and Q.
- Second line : N space separated integers denoting array A.
- Next Q lines : Two space separated integers L and R.

## Output format

Output the result of each query in a separate line.
