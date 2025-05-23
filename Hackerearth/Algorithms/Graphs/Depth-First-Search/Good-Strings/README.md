# [Good strings][link]

There is a string consisting of only three characters (, ) and #.

For Example:

-     s   = ((#)(#))
      idx = 12345678

Here, the bracket pairs are 1 -> 8, 2 -> 4, and 5 -> 7 and each bracket pair can have some non - negative value associated with it.

You can categorize the bracket pair and # into two categories alpha and beta. # are also associated with some non-negative values which will be provided in the input.

Now you have to assign the category to each of the characters (i.e. alpha or beta) and non-negative values to the bracket pair such that the given string is the good string.

The good string is the string if the gamma values for each of the bracket pair is equal to Vali (Vali is provided in the input).

Gamma value is the sum of all the values of the character contained in the bracket pair whose category is the same as the category of the current bracket pair.

## Input format

- The first line of the input contains an integer n (length of the string).
- The second line of the input contains the string of length n.
- Now let the number of # in the string be x, So next x lines will be containing two integers indx and val each, here indx is the index of the # and val is the value corresponding to that #.
- Now let the number of bracket pairs in the string be y, So next y lines will be containing 3 non-negative integers start, end, and Val. Here start is the starting index of that bracket pair, the end is the index of the ending of that bracket pair and Val is the expected gamma value of that bracket pair after performing the operations of categorizing the characters and assigning the values to the bracket pairs.

## Output format

Print "Yes" if it is possible to make it the string good otherwise print "No". (without quotes).

[link]: https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/check-the-string-0d25fff4/
