# [Replace][link]

In this problem the word "set" will always denote a multiset (link to wikipedia). Thus, some of its elements can be the same. The order of elements doesn't matter. Multisets {a, a, a, b, c, b} and {a, b, c, a, b, a} are the same. Multisets {a, a, b} and {a, b, b} are different.

You have a set consisting of some elements. A set can either be empty, or contain other sets. Note that sets in this problem may contain multiple copies of the same set. More formally, a set satisfies the following context free grammar with start symbol S:

S -> {T}
T -> ST | ε

In this context free grammar, S denotes a set, while T denotes a list of the elements which are sets themselves. For example, valid sets are {}, {{}}, {{}{}}, {{}{{}{}}}.

We can define an element of a set to be one of the sets that make up the set. For example, a set {a, a, b} has three elements, that is a, a, and b. The set {} has no elements. The set {{}} has one element {}. The set {{}{{}{}}} has two elements {}, {{}{}}.

Two sets are said to the same if they have the same multiset of elements. Note that the order of elements in the sets doesn't matter. For example, the sets {{}{{}}} and {{{}}{}} are the same, but the sets {{}{}} and {{}} are different.

Call a set S transitive if x is an element of S, then all elements in x are elements of S as well.

For example, the empty set {} is transitive. The set {{}} is also transitive. However, the set S = {{{}}} is not transitive, as {{}} is an element of S, but {} is an element of {{}} but not of S. We can make it transitive by adding the element {} to the set to get the transitive set {{{}}{}}.

You’re given a string with n characters representing a set. You would like to make this set transitive with the minimum number of moves. In one move, you can either add an arbitrary set or remove an arbitrary element from S. You are not allowed to add or remove elements in sets that are elements of S. Compute the minimum number moves you need to make the set transitive.

## Input format

- The first line of the input will contain an integer T, denoting the number of test cases.
- Each test case will contain a single string on its own line, denoting the set.

## Output format

Print a single line per test case, the minimum number of moves required to make the set transitive.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/maximum-flow/practice-problems/algorithm/replace/
