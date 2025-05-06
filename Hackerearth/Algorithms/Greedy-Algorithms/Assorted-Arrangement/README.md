# [Assorted Arrangement][link]

You have a set of n distinct positive numbers. You also have m colors. Your colors are labeled from 1 to m. You're also given a list c with m distinct integers.

You paint the numbers according to the following rules: For each i in order from 1 to m, paint numbers divisible by c[i] with color i. If multiple rules apply to a number, only the last rule applies.

You sorted your set of numbers and painted them. It turns out that no number was left unpainted. Unfortunately, you lost the set of numbers you had originally. Return the smallest possible value of the maximum number in your set. The input will be constructed such that it's guaranteed there is at least one set of numbers that is consistent with the given information.

## Input format

- The first line will contain two space separated integers n,m.
- The second line will contain m space separated integers. The i-th integer in this line denotes c[i].
- The third line will contain n space separated integers. This j-th integer in this line denotes the color of the j-th smallest number in your set.

## Output format

Print a single integer on its own line, the minimum possible value of the largest number in your set.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/assorted-arrangement-3/
