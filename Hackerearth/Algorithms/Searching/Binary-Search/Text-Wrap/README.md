# [Text Wrap][link]

Prakhar has a string with N words where the length of the i-th word is L[i].

The words are displayed in the window separated by a space. More precisely, when the sentence is displayed in a window of width W, the following conditions are satisfied.

- The first word is displayed at the beginning of the top line.
- The i-th word (2 <= i <= N) is displayed either with a gap of 1 after the (i-1)-th word, or at the beginning of the line below the line containing the (i-1)-th word.
- The width of each line does not exceed W. Here, the width of a line refers to the distance from the left end of the leftmost word to the right end of the rightmost word.
- A word should not be broken into 2 or more lines.

Prakhar Wants to fit these words in M or less than M lines, find the minimum possible width W of the window.

## Input format

- The first line contains 2 space seperated integers N - the total number of words and M - the required number of lines.
- The next line contains N space seperated integers L[i]

## Output format

Print the minimum possible width W of the window

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/minimum-width-3ae6ed73/
