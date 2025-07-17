# [Xsquare And Balanced Strings][link]

Xsquare got bored playing with the arrays all the time. Therefore he has decided to buy a string S consists of N lower case alphabets. Once he purchased the string, He starts formulating his own terminologies over his string S. Xsquare calls a string str A Balanced String if and only if the characters of the string str can be paritioned into two multisets M1 and M2 such that M1= M2 .

For eg: Strings like "abccba" , "abaccb" , "aabbcc" are all balanced strings as their characters can be partitioned in the two multisets M1 and M2 such that M1 = M2.

- M1 = {a,b,c}
- M2 = {c,b,a}

whereas strings like ababab , abcabb are not balanced at all.

Xsquare wants to break the string he has purchased into some number of substrings so that each substring is a balanced string . However he does not want break the string into too many substrings, otherwise the average size of his strings will become small. What is the minimum number of substrings in which the given string can be broken so that each substring is a balanced string.

## Input format

- First line of input contains a single integer T denoting the number of test cases.
- First and the only line of each test case contains a string consists of lower case alphabets only denoting string S.

## Output format

For each test case, print the minimum number of substrings in which the given string can be broken so that each substring is a balanced string. If it is not possible the given string according to the requirement print -1.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/xsquare-and-balanced-strings/
