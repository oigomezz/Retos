# Monk Celebrating Checkpoint

Monk is feeling happy to reach the first checkpoint in his journey. in order to have fun, he asked Mishki to solve a problem for him.

She will be given an array of N distinct elements, and needs to perform at most X arbitrary operations. In each operation she can select any element from the array and can increase it by exactly 1. She can perform at max 1 operation over any element of the array.

The special thing about this array is that, for any 2 elements (A[i], A[j]), where i != j, abs(A[i] - A[j]) >= K, where abs(x) denotes the absolute value of any integer x.

Now, we define 3 functions:

- F(i,j) = Max(i,j) - Min(i,j)
- Max(i,j): = Maximum element present in the sub array ranging from i, i+1, ... , j in array A.
- Min(i,j): = Minimum element present in the sub array ranging from i, i+1, ... , j in array A.

Mishki needs to perform exactly X operations, and then needs to tell Monk the following:

    answer = ΣΣ F(i,j)

In short, she needs to tell Monk the summation of the difference between the maximum and minimum element of each sub array of array A . Considering Mishki performs the X operations given to her optimally what is the maximum value of answer that she can achieve ?

Help Mishki for the same.

## Input format

- The first line will consists of 3 space separated integers N, X and K , denoting the number of elements in the array, operations needs to be performed and minimum absolute difference between any 2 elements of the array respectively.
- In next line, there will be N space separated integers, A[i], where 1 <= i <= N, denoting the elements of array.

## Output format

Print the required maximum possible maximum value of answer.
