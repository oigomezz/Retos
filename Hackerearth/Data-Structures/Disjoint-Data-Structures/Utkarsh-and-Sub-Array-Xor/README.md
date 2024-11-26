# Utkarsh and Sub Array Xor

Utkarsh loves binary sequences. Once he was playing with his favorite binary sequence of length N. But somehow he misplaced it. He remembers the bitwise XOR of exactly K subarrays. Utkarsh fears that you will steal his sequence so he will not reveal the actual XOR value of any sub array.

He plans to recover the sequence using this information only. You being his best friend will convince him there are just too many sequences satisfying the Sub Array Xor and its better to forget his love for that sequence.

## Input format

- The first line contains N and K.
- K lines follow. Each line contains two integers u v denoting S[u] XOR .. XOR S[v] is known.

## Output format

Print K integers, ith integer being the maximum number of binary sequences of length N satisfying first i XOR constraints. As the answer can be large, output each result mod 10⁹+7
