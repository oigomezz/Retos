# [String Paradigm][link]

You are given a string S of length N having distinct lowercase alphabetic characters. Each character in the string S has some follow-up characters. The follow-up character denotes what characters can follow a particular character that belongs to the string S. Note that the follow-up characters belong to the string S.

Now you have to pick one of the characters of the string S and mark it as a start character. After you pick one character, you need to look in its follow-up list and choose one character from it and continue this to form a new string.

Now, you have to count the total number of non-empty subsequences of all the possible M length strings that can be made out of the characters of the string S. Since the number could be very large output it modulo 10⁹ + 7.

**Note:** Carefully check out the sample explanation for a better understanding of the problem.

## Input format

- The first line of the input contains a single integer N, the length of the string.
- The second line of the input contains a string S of length N.
- Then N lines follow, i-th line contains a string Ti where each character in the string is a follow up character of the i-th character in the main string S.
- The last line contains a single integer M, length of the string that has to be constructed.

## Output format

The only line of the output contains a single integer, the total number of non-empty subsequences of all the possible M length strings modulo 10⁹ + 7.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/2-dimensional/practice-problems/algorithm/string-paradigm-c88e11d6/
