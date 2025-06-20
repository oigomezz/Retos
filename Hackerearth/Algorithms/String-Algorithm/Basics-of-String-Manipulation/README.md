# Basics of String Manipulation

A string is a sequence of characters. In other words, a string is an array of character data type. An instance of a string is called a string literal. For instance in C++: string s = "HackerEarth"; s is a string literal.

String Manipulation is a class of problems where a user is asked to process a given string and use/change its data. An example question would be a great way to understand the problems that are usually classified under this category.

- Given a string S of length N, shift each character of the string by K positions to the right, where K <= N.

For example: Say S = "hacker" and K = 2. Here N = 6.

Shifting each character in S by 2 positions to the right would result into erhack.

Note that S[0] i.e. 'h' is moved by 2 positions to the S[2]. Also, S[5] i.e. 'r', which is the last character in S comes round-about back to S[1] as there is no space for 'r' to go beyond the limits of string length.

## Approach

- Declare another auxillary string shiftedS that is of the same size as S.
- Copy i-th element of S to the (k+i)th position in shiftedS. This means, shiftedS[i+K] = S[i] where 0 <= i < N.
- Make sure that i+K never exceeds M, because that will try to access a memory location which is not declared in shiftedS. There's a simple trick to ensure that - use (i+K) mod N.

## Implementation

```c++
void shiftByK(char S[], char shiftedS[], int N, int K) {
    // Iterate through the length of given string
    for(int i=0; i<N; i++) {
        // Find the index for this current character in shiftedS[]
        int idx = (i+K) % N;
        // Copy that character at the found index idx
        shiftedS[idx] = S[i];
    }
    // Add a NULL character to mark the end of string
    shiftedS[N] = '\0';
}
```

Every character array in C/C++ ends with a '\0' (NULL) character. It marks the end of the string. If it is not added in the end, then the code may produce garbage characters after the string.
