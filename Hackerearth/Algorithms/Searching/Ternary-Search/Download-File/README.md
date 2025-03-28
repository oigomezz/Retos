# [Download file][link]

Hasan wants to download a file from the internet, the file size is S MB, the internet speed available for Hasan is not fixed, it can be changed by time.

Hasan knows a list of times when the internet speed will be changed and the new speed for each time. more specifically Hasan has two arrays for length N which means:

starting from time T0 the internet speed is D0 MB per unit time. and starting from T1 the internet speed is D1 MB per unit time. and so on

it is provided that T0=0

Hasan wants the download duration be minimum possible (i.e. duration between starting of download and the end of download be minimum), note that Hasan can choose when to start the download but once it started it cannot be paused, it will continue until the end. Help Hasan by telling him what is the minimum possible duration that he can Achieve.

## Input format

- First line contains two integers N and S.
- The following N lines, each contains two integers Ti and Di

## Output format

Output a irreducible fraction,donating the minimum duration required to download the file if starting time is chosen optimally, in this format: a/b

[link]: https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/download-file-b0fe3520/
