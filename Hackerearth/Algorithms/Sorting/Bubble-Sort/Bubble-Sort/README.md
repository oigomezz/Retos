# [Bubble Sort][link]

You are given arrays A[1], A[2], ..., A[N]. What will return the next function Bubble Sort(A)

```c
int bubble_sort(int A[]){
  int count = 0;
  int n = length(A);
  bool swapped = true;
  while (swapped){
    swapped = false;
    count++;
    for (int i = 0; i < n; i++){
      if (A[i] > A[i + 1]){
        swap(A[i], A[i + 1]);
        swapped = true;
      }
    }
  }
  return count;
}
```

## Input format

- The first line contains the integer N denoting the number of elements of array A.
- The second line contains N positive integers denoting the elements of the array.

**Note:** It is guaranteed that all elements of array are different.

## Output format

Print an integer that denotes the answer to the question.

[link]: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/bubble-sort-15-8064c987/
