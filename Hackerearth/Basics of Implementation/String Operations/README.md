# String Operations

You are given a string S.

Q number of operations are performed on string S.
In each of these Q operations, you are given an index ind and a character ch. For each operation, you have to update character at index ind in string S to ch, that is, after this operation S[ind] = ch.
It is guaranteed that any index is updated atmost once.
We call the final string after performing Q number of operations as str.

After this, M number of operations are performed on string str.
In each of these M operations, you are given two indices a and b. For each operation, you have to reverse the substring that lies between the indices a and b (inclusive).
We call the final string after performing M operations as fin.

Example: If string is "xyz" and one of the Q operations is 1 a, then string "xyz" now becomes "ayz" as S[1] = a after the operation.
one of the M operations is 1 3, then "ayz" now becomes "zya" as the substring lying between indices 1 and 3 is reversed.

You have to print string str, string fin and the number of indices which have same characters at them in both strings str and fin.

## Input format

- First line consists of string S.
- Next line consists of an integer denoting Q.
- Following Q lines contain two integers each: ind and ch.
- Next line consists of an integer denoting M.
- Following M lines contain two integers each: a and b.

## Output format

In first line, print string str.
In second line, print string fin.
In third line, print the number of indices which have same characters at them in both strings str and fin.
