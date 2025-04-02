# TUTORIAL Quick Sort

Quick sort is based on the divide-and-conquer approach based on the idea of choosing one element as a pivot element and partitioning the array around it such that: Left side of pivot contains all the elements that are less than the pivot element Right side contains all elements greater than the pivot

It reduces the space complexity and removes the use of the auxiliary array that is used in merge sort. Selecting a random pivot in an array results in an improved time complexity in most of the cases.

## Implementation

Select the first element of array as the pivot element First, we will see how the partition of the array takes place around the pivot.

In the implementation below, the following components have been used: Here, A[] = array whose elements are to be sorted

- start: Leftmost position of the array
- end: Rightmost position of the array
- i: Boundary between the elements that are less than pivot and those greater than pivot
- j: Boundary between the partitioned and unpartitioned part of array
- piv: Pivot element

```c
int partition ( int A[],int start ,int end) {
    int i = start + 1;
    int piv = A[start]; // make the first element as pivot element.
    for(int j =start + 1; j <= end ; j++ )  {
    /*rearrange the array by putting elements which are less than pivot
       on one side and which are greater that on other. */
          if ( A[ j ] < piv) {
            swap (A[ i ],A [ j ]);
            i += 1;
        }
   }
   swap ( A[ start ] ,A[ i-1 ] ) ;  //put the pivot element in its proper place.
   return i-1;                      //return the position of the pivot
}
```

Now, let us see the recursive function Quick_sort:

```c
void quick_sort ( int A[ ] ,int start , int end ) {
   if( start < end ) {
        //stores the position of pivot element
         int piv_pos = partition (A,start , end ) ;
         quick_sort (A,start , piv_pos -1); //sorts the left side of pivot.
         quick_sort ( A,piv_pos +1 , end) ; //sorts the right side of pivot.
   }
}
```

Here we find the proper position of the pivot element by rearranging the array using partition function. Then we divide the array into two halves left side of the pivot (elements less than pivot element) and right side of the pivot (elements greater than pivot element) and apply the same step recursively.

**Complexity:** The worst case time complexity of this algorithm is O(N²), but as this is randomized algorithm, its time complexity fluctuates between O(N²) and O(Nlog(N)) and mostly it comes out to be O(Nlog(N)).
