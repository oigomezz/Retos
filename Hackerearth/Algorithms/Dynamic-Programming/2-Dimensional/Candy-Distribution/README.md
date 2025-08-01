# [Candy Distribution][link]

It's your birthday today, right? If it is, then we wish you Happy Birthday and good luck in the contest. But, even if it is not, you have to be ready to give candies to your friend when this day comes!

You have N candies to distribute and you decide to give them to anyone who shows up. Because this is your day, you invented your own method of distributing all these candies . The process is the following:

Initially, there are N candies placed in one pile. While there are any candies left, a person shows up and do the following:

1. Picks up the first pile with candies, let's call this pile P.
2. If P has one or two candies, he takes all the candies from P. Otherwise, he takes just one candy, divide the rest into some number of piles, at least 2, of equal sizes and put them in front the other piles.

Because at HackerEarth we like math, we are interested how many different such processes are there. We consider two processes different if and only if one distributes candies to different number of people than the other or both distribute candies to the same number of people and there exists a person who decides to distribute candies differently in them. You have to return the number of different such processes modulo M = 10⁹ + 7.

## Input format

- In the first and only line there is one integer N.

## Output format

In one line output a single integer - the answer to the problem modulo M = 10⁹ + 7 .

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/candy-distribution/
