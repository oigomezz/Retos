# TUTORIAL Basics of Implementation

Questions that are based on ad-hoc ideas and brute-force solutions are usually classified under the implementation category. The objective of such questions is to help users to improve their ability of converting English statements into code implementation.

This tutorial discusses 2 kinds of problems that will help you get started with such questions.

**Question 1** You are given two numbers N and M, print the absolute difference between two numbers i.e. |N- M|.

Approach:

- Store the difference of N and M in a temporary variable result.
- Check if the value of result is negative.
- The question is to print the absolute difference. Therefore, if the value is negative, then make it positive by multiplying it with -1.
- Print out the value of result.

Implementation

```c
#include <iostream>
using namespace std;

int main() {
    int n, m;
    // Read the two numbers from STDIN
    cin >> n >> m;
    // Store the difference between them in result
    int result = n - m;

    // If result is negative multiply it with -1
    if(result < 0) {
        result = result*(-1);
    }

    // Print the result to STDOUT
    cout << result;
    return 0;
}
```

**Question 2** You are given a string S, which comprises English alphabets, determine the count of all the vowels in S. Vowels are [a,e,i,o,u]. Print the count of all the vowels that are available in the string S.

Approach:

- There are five vowels in English alphabet. Declare variables for five integers and initialize them as 0.
- Traverse the string S, character by character, check if the character is vowel. If it is, increment the count of that vowel by 1.
- Print out the count of each vowel after the iteration over the string is done.

Implementation

```c
#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Declare variables to store count of vowels
    int a = 0, e = 0, i = 0, o = 0, u = 0;
    string s;
    // Read given string from STDIN
    cin >> s;

    int s_len = s.length();
    // Iterate over each character in the string
    for(int j=0; j<s_len; j++) {

        // This can be done in a better way using hashing, which simplifies the implementation,
        // however for the purpose of this article we'll restrict the implementation to naive way

        // Check for each character in if else
        if(s[j] == 'a') {
            a++;
        } else if(s[j] == 'e') {
            e++;
        } else if(s[j] == 'i') {
            i++;
        } else if(s[j] == 'o') {
            o++;
        } else if(s[j] == 'u') {
            u++;
        }
    }
    // Print out the result to STDOUT
    cout << "a " << a << endl;
    cout << "e " << e << endl;
    cout << "i " << i << endl;
    cout << "o " << o << endl;
    cout << "u " << u << endl;
    return 0;
}
```
