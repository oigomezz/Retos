# [Number of R's][link]

As we all know RK loves his name very much especially the character 'R' so this time task for you is based on his awesome name. RK gives you a string S consisting of characters 'R' and 'K' only. Now you are allowed to do exactly one move that is you have to choose two indices i and j (1<= i<=j<= |S| where |S| is string length) and flip all the characters at position X where i<=X<=j. Flipping the character means:

     if S[X]='R' :  //If character at position X is 'R' then change it to 'K'
          S[X]='K'
     else :          //else if character at position X is 'K' then change it to 'R'
          S[X]='R'

Now your goal is that after exactly one move you have to obtain the maximum number of R's as RK loves this character very much. So help RK with maximum R's.

## Input format

- The first line contains the number of test cases T.
- Each test case contains a string S consisting of characters 'R' and 'K' only.

## Output format

For each test case print the maximal number of R's that can be obtained after exactly one move.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/number-of-rs-1/
