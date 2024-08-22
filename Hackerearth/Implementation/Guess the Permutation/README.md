# Guess the Permutation

In this problem your goal is to guess some secret permutation A of integers from 1 to 16.

There are 17 tests in this problem. Test number i for 1 <= i <= 16 will have the following form:

- The first line of the input contains string "ELEMENT" (without quotes)
- The second line of the input of the test i contains two integers from 1 to 16 each - i and element A[i] of the secret permutation
- The only line of the output file contains one integer - A[i] too.

Input of the last (the 17-th test) will contain the only string "PERMUTATION" (without quotes). For this test your program should output some permutation of integers from 1 to 16 - your variant of the secret permutation.

If this permutation equals to the secret permuation A and passes all the 17 tests with your solution , you will receive 100 points. Otherwise you will receive 0 points. Note that for each wrong try you will receive 20 minutes penalty time after you solved this problem (as in ACM ICPC format)
