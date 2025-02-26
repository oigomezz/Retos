# Monk and Sorting Algorithm

Monk recently taught Fredo about sorting. Now, he wants to check whether he understood the concept or not. So, he gave him the following algorithm and asked to implement it:

**Assumptions:** We consider the rightmost digit of each number to be at index 1, second last at index 2 and so on till the leftmost digit of the number.

Meaning of i-th chunk: This chunk consists of digits from position 5 \* i to 1 + 5 \* (i -1) in the given number.If there is no digit at some position in the number, take the digit to be 0.

Initially, i is 1.

- Construct the i-th chunk, for all of the integers in the array. Let's call the value of this chunk to be the weight of respective integer in the array.
- If weight of all the integers of the array is 0, then STOP
- Sort the array according to the weights of integers. If two integers have same weight, then the one which appeared earlier should be positioned earlier after the sorting is done. The array changes to this sorted array.
- Increment i by 1 and repeat from STEP 1

See the sample explanation for a better understanding.

So, Fredo understood the concept and coded it. Now, Monk asks you to write the code for the algorithm to verify Fredo's answer

## Input format

- The first line of the input contains N denoting the number of elements in the array to be sorted.
- The next line contains N single space separated integers denoting the array elements.

## Output format

You need to print the new array in each step of the algorithm.
