# [Partition it!][link]

Tubby the doggu, likes sets which are closed. Your task is to help him/her solve a problem.

Let's first lay out a few definitions:

**Definition 1:** A set S is said to closed with respect to a prime number P if and only if:

a \* b (mod P) ∈ S, ∀a,b ∈ S.

Note that a,b can be equal.

**Definition 2:** Closure(S): Closure of a set S is defined to be the smallest closed set containing the set S.

**Definition 3:** Partition(S): Partition of a set S is a set of non-empty subsets of S such that every element of S is in exactly one of these subsets. Moreover, the length of the partition is the number of non-empty subsets required.

Now the task is that you are given a prime number P and an array A of N integers, in which the i-th integer is denoted by Ai, 1 <= i <= N, 1 <= Ai < P.

You have to partition the set of indices {1,2,3,4,..., N} into a partition of minimum length such that if Closure({Ai} ⊆ Closure({Aj})) then i and j must be in different sets of the partition.

Here, i != j, 1 <= i,j <= N.

**Note:** x denotes a set containing a single element x.

## Input format

- The first line will consist of the integer T denoting the number of test cases.
- For each of the T test cases, the first line will consist of two integers P and N, where P is a prime number and N denotes the number of elements.
- Next line will consist of N integers, where the i-th integer denotes the element Ai, 1 <= i <= N.

## Output format

For each of the T test cases, output a single integer denoting the minimum length of the partition.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/topological-sort/practice-problems/algorithm/partition-it-4cc63265/
