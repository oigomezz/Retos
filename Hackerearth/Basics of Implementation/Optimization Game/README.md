# Optimization Game

Currently, Monk is playing a unique kind of strategy game called optimisation game. In this game we are provided with an array containing integral numbers. Now all these numbers represent the count of their respective index power of 2. The goal of the game is to minimize the total sum of the count of the array by converting lower powers of 2 into their higher powers i.e. for example 2. Note that we can extend the array beyond the final index i.e. N - 1 too in case it optimizes our result. Please see the below example for more understanding.

Let the number of elements given in the initial array be 3. Consider the array to be [1,2,0]. It means that 2^0 has count = 1,
2^1 has count = 2, 2^2 has count = 0.

Now, we can convert 2 \* 2^1 into 1 2^2 as 2^1 \* 2 = 2^2. We get the new array as [1,0,1]. Now the total sum is 1 + 0 + 1 = 2 which is the required minimum value obtained at the end of the game as we can't reduce it any further.

## Input format

- First line will contain the number of test cases as T.
- For each of the test case, N will be given in the first line and N integers will be given in the second line.

## Output format

Output the minimum value obtained after playing the optimization game in a separate line for each test case.
