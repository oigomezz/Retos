# [Vowel Query][link]

You are given a string S consisting of lowercase alphabets and an integer array val consisting of N integers. Using the given string S and array val, you need to create another string X according to the code snippet below:

Initially string X is empty

Let len be the length of string S

    for i := 0 to N-1
        pos := absolute value of val[i]
        if(val[i] >= 0)
          X := X + S[0,pos] // append substring of string S from index 0 to pos (both including) into X
        else
          X := X + S[pos,len-1] // append substring of string S from index pos to len-1 (both including) into X

You have to answer Q tasks. For each task, you are given an integer K and you have to print the Kth vowel in the string X. If the Kth vowel doesn't exist print -1.

**Note:** The vowels are a, e, i, o, and u.

## Input format

- The first line contains a string S.
- The second line contains an integer N.
- The third line contains N space-separated integers, denoting the element of the array val.
- The fourth line contains an integer Q, denoting the number of tasks.
- The fifth line contains Q space-separated integers, denoting the tasks.

## Output format

Print the answer for each of the Q tasks in a newline.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/vowel-query-51648a6c/
