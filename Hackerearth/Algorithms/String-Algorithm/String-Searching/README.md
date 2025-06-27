# String Searching

## String Searching by KMP algorithm (Knuth Morris Pratt algorithm)

**Motivation Problem:** Given 2 strings P (pattern) and T (text), find the number of occurrences of P in T.

### Basic / Brute Force solution

One obvious and easy to code solution that comes to mind is this: For each index of T, take it as a starting point and find if T[i:i+|P|-1] is equal to P.

```Python
for i = 0 to length(T)-length(P):
    Found = true
    for j = i to i + length(P) - 1:
        if P[j-i] not equal to T[j]:
            Found = False

    if Found = True
        answer = answer + 1
```

This brute force takes time in the worst case, which is obviously too slow for large strings.

### Knuth Morris Pratt Algorithm

Suppose for each index i of some string Z, the longest suffix in Z[0:i] that is also a prefix of Z[0:i], be known. Formally, a length Fi is known such that Z[0:Fi-1] = Z[i-Fi+1:i]. Let these lengths be stored in array F. The suffix needs to be proper(whole string is not a proper suffix).

Then the solution to the motivation problem can be found as follows:

Define a string V = P + '#' + T, where '#' is a delimiter that is not present in either of P or T. Now, if the above information is known, all occurrences of P in T can be found as follows: If at some index i, Fi = |P|, then there is an occurrence of Pattern P at position i - |P| +1. All such indices from |P| + 1 [0 based indexing, the index just after '#'], need to be checked.

The main part of KMP algorithm calculates the array F, which is also called the prefix function. If calculation of F or the prefix function can be done efficiently, then we have an efficient solution to the motivation problem. KMP algorithm finds the prefix function in O(length_of_String) time.

To find the prefix function, best possible use of previous values of array F is made, so that calculations aren't done again and again. Suppose all Fi have been calculated, and now Fi+1 is to be calculated. It is to be noted that, value of Fi+1 can be at most 1 greater than Fi. Here is a proof by contradiction:

Suppose F[i+1] > F[i] + 1. Now, if the (i+1)th character is removed, we obtain a suffix ending at index i that is of length F[i+1] - 1, which is greater than Fi. This is a contradiction, hence proved.

Observe that if Z[i+1] = Z[Fi], then the value of F[i+1] = F[i] + 1. If not, a smaller suffix ending at index i is to be found, that is also a prefix of Z[0:i]. Let the length of such a suffix be j, then if Z[i+1] = Z[j] then F[i+1] = j + 1. If again the equality doesn't hold true, smaller and smaller suffixes that end at index i, which are also prefixes of Z[0:i] need to be found.

The only thing remaining is, how to find the length of next smaller suffix ending at index i, that is also a prefix? This is also pretty simple. Observe that due to the property of F, the segment Z[0:Fi-1] is equal to the segment Z[i-Fi+1:i]. So to find the next smaller suffix ending at index i, the longest suffix ending at F[i]-1 can be found which is F[F[i] - 1], and this suffix will be the next smaller suffix ending at index i. If this suffix also doesn't satisfy our criteria, then smaller suffixes can be found with the same process, here it will be F[F[F[i]-1]-1]. Note that, if at some point the length becomes 0, the process is stopped.

This completes KMP algorithm. Below is the code

```c++
vector<int> prefix_function (string Z) {
    int n = (int) Z.length();
    vector<int> F (n);
    F[0]=0;
    for (int i=1; i<n; ++i) {
        int j = F[i-1];
        while (j > 0 && Z[i] != Z[j])
            j = F[j-1];

        if (Z[i] == Z[j])  ++j;
        F[i] = j;
    }
    return F;
}
```
