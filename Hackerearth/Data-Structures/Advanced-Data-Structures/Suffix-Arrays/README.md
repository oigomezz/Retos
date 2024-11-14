# TUTORIAL Suffix Arrays

**Motivation Problem:** Given a string S, find the longest sub string that occurs at least M times.

**Brute Force method:** For every sub string X of S, one can find all the occurrences of X in S by KMP. KMP takes O(N) time, so the total time for this brute force method will be O(N³).

## A faster solution using hashing

We can binary search the length of the sub string. For a current length X in the binary search, hash of every sub string of length X can be found in O(N) time. While doing this, the hashes can be stored in a dictionary, and when all sub strings of length X are processed, the hash with maximum frequency is to be checked if it has frequency greater than equal to M. This takes O(N(logN)²) time, where a log term comes due to maintaining the dictionary(map in C++).

## A solution using Suffix Array

A Suffix Array is a sorted array of suffixes of a string. Only the indices of suffixes are stored in the string instead of whole strings. For example: Suffix Array of "banana" would look like this:

        5 => a
        3 => ana
        1 => anana
        0 => banana
        4 => na
        2 => nana

One naive way to make the suffix array would be to store all suffixes in an array and sort them. If we use an O(N logN) comparison based sorting algorithm, then the total time to make the suffix array would be O(N² logN), because string comparison takes O(N)time. This is too slow for large strings.

Below is shown an O(N (logN)²) algorithm that constructs the suffix array. There is an O(N logN) algorithm and even an O(N) algorithm to construct suffix array, but in a programming contest environment, it is much easier to implement an O(N (logN)²) algorithm. Also the difference between an O(N (logN)²) and O(N logN) algorithm is scarcely noticeable for strings up to length 10⁵.

The algorithm is based on keeping the ranks of suffixes when the suffixes are sorted by their first
characters in the step. Therefore we will execute O(logN) steps to completely build the suffix array.

It can be easily seen that, comparison of 2 strings should be optimised, and should be done in better than O(N). It can actually be done and the string comparison of 2 suffixes can be done in O(1)time. To do this, the fact that 2 suffixes of the same string are being sorted should be used.

Here is some pseudo code to construct suffix array.

```Python
    SA = [] # Suffix Array
    P = [][] # P[i][j] denotes rank of suffix at position 'j' when all suffixes are sorted by their first '2^i' characters
    str = [] # initial string, 1 based indexing
    POWER = [] #array of powers of 2, POWER[i] denotes 2^i

    tuple {
        first, second, index;
    }

    L = [] # Array of Tuples
    N = length of str
    for i = 1 to N:
        P[0][i] = str[i] - 'a' # Give initial rank when suffixes are sorted by their first 2^0 = 1 character.

    step = 1
    for i = 1; POWER[i-1]<N; i++, step++:
        for j = 1 to N:
            L[j].index = j
            L[j].first = P[i-1][j]
            L[j].second = (j+POWER[i-1]<=n ? P[i-1][j+POWER[i-1]] : -1)

        sort(L)
        for j = 1 to N:
            P[i][L[j].index] = ((j>1 and L[j].first==L[j-1].first and L[j].second==L[j-1].second) ? P[i][L[j-1].index] : j)
            /*Assign same rank to suffixes which have same number in the first and second fields of their respective tuples.*/
    step = step - 1
```

Now at the step-th row of matrix P, we have the ranks of all suffixes. Now we can get the suffix array very easily in O(N).

```Python
    for i = 1 to N:
        SA[P[step][i]] = i
```

**Note:** Care must be taken when string length is 1, in that case if the string is "c", then it will get a rank of ('c'-'a') that is 2 because we will not enter the for loop. In this case you can manually put the rank as 1, that is P [0] [1] = 1 instead of P [0] [1] = str[1] - 'a'.

Often it is required to find the Longest Common Prefix (LCP) of 2 suffixes. This can be done easily in O(logN) time by using the array P. The following fact is used to find the LCP of 2 suffixes starting at indices i and j: If P [x] [i] == P [x] [j], then first 2^x characters starting at indices i and j are same. Below is the pseudo code:

```Python
LCP(i,j): # returns the length of LCP of suffixes starting at indices i and j
    if i==j:
        return N-i+1
    return_value=0

    for x = step to 0:
        if P[x][i]==P[x][j]:
            return_value = return_value + POWER[x]
            i = i + POWER[x]
            j = j+ POWER[x]
    return return_value
```

Now coming to the original problem, to find the longest sub string that occurs at least M times.

First build the suffix array of string S. If in the sorted array of suffixes, the LCP of 2 suffixes is K, then the prefix of length K of all suffixes between these 2 suffixes is same. Let index of these 2 suffixes be i and j (i < j), then a sub string of length K repeats (j - i + 1) times.

To find the solution to motivation problem, one can iterate through all the suffixes in sorted order from 0 to (N - M + 1), and find the LCP of current suffix and suffix at index (M-1) greater than it. This LCP will repeat at least M times, and the maximum of all these LCPs can be taken. Time complexity: O(N(logN)²).

```Python
build Suffix Array

for i = 1 to (N-M+1):
    ans=max(ans, LCP(SA[i],SA[i+M-1]))
```
