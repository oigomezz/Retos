# [Friendly Neighbors][link]

HackerEarth City can be represented as an infinite number of houses standing next to each other and numerated starting with 1 from left to right. Recently n people have decided to move in HackerEarth City. They haven't decided which houses to accommodate yet, so they kindly asked for your help.

You have n non-empty sets of positive integers S1,S2,...,Sn. The i-th person can live in any house from the set Si. You have to choose a house for each person. More formally, you have to create an array A[1], A[2], ..., A[N] such that for all i, Ai ∈ Si and Ai denotes the house of the i-th person.

Since all of them are close friends, they always attend their neighbor's birthdays. Let Bi denote the distance between i-th person and the closest neighbor to his left (some person j != i such that Aj < Ai and Aj is maximum). If he doesn't have any such neighbor, we say that Bi = 0. Let Ci equivalently denote the distance to the closest neighbor to his right.

You would like to create A[1], A[2], ..., A[N] in such a way that ΣB + ΣC is minimized.

Find and print the minimum possible value of ΣB + ΣC.

## Input format

- The first line of the input contains a single integer the number of testcases.
- Description of t independent testcases follow. For each individual test, a single line contains one integer n, the number of sets.
- Next n lines describe the sets. The i-th line contains the description of in the following format: k, S(i,1), S(i,2),..., S(i,k) . Here, k is the size of Si.
- It is guaranteed that every pair of sets has an empty intersection (for each 1 <= i < j <= n, Si ∩ Sj != 0). Also, it is guaranteed that Σn and Σk over all sets over all testcases does not exceed 10⁵.

## Output format

The output should contain t integers, each in a new line the minimum possible value of ΣB + ΣC for each testcase.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/choose-one-c4672347/
