# [Caesar's Cipher][link]

Caesar's Cipher is a very famous encryption technique used in cryptography. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, D would be replaced by G, E would become H, X would become A and so on.

Encryption of a letter X by a shift K can be described mathematically as Ek(X) = (X + K) % 26.

Given a plaintext and it's corresponding ciphertext, output the minimum non-negative value of shift that was used to encrypt the plaintext or else output -1 if it is not possible to obtain the given ciphertext from the given plaintext using Caesar's Cipher technique.

## Input format

- The first line of the input contains Q, denoting the number of queries.
- The next Q lines contain two strings S and T consisting of only upper-case letters.

## Output format

For each test-case, output a single non-negative integer denoting the minimum value of shift that was used to encrypt the plaintext or else print -1 if the answer doesn't exist.

[link]: https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/caesars-cipher-1/
