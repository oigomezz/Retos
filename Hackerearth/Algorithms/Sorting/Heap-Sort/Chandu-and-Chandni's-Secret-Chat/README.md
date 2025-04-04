# [Chandu and chandni's secret chat][link]

Chandu and chandni Talk on phone for a long time daily. Being afraid that someone will hear their private conversation chandu suggested chandni an idea. He suggested that he will talk only with encrypted strings with her and only she would know, how to decrypt the string. So that even if someone hears, He/She would not be able to anticipate their conversation.

Rules of encryption are as follows:

1. String on length N is assumed to be cyclic consisting of lower case English alphabets.
2. In each iteration, we pick the last character and put it in starting of the string. For example: april performing iterations and collecting each string formed in a set until we get the original string. Ex: {april,lapri, ilapr, rilap, prila}
3. sort the set of string in lexicographically reverse order. Ex: {rilap, prila,lapri, ilapr, april }
4. Taking the last character of each string in the set is the encrypted string. Ex: pairl

Chandu also sends the position(K) of first letter in encrypted string from original string i.e 2 (p is on position 2 in original string and is the first character of encrypted string)

Now, Chandni is ofcourse not that brilliant to decrypt the strings in real time and understand what chandu is saying. So, chandu decided to write a program for the same.

Help chandu write this program.

## Input format

- First line contains an integer t, which is the number of test cases.
- Next t lines contain a encrypted string and K as decribed above.

## Output format

Print the decrypted string for each test case.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/heap-sort/practice-problems/algorithm/chandu-and-chandnis-secret-chat/
