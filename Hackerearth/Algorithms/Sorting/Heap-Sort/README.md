# TUTORIAL Heap Sort

Heaps can be used in sorting an array. In max-heaps, maximum element will always be at the root. Heap Sort uses this property of heap to sort the array.

Consider an array Arr which is to be sorted using Heap Sort.

- Initially build a max heap of elements in Arr.
- The root element, that is Arr[1], will contain maximum element of Arr. After that, swap this element with the last element of Arr and heapify the max heap excluding the last element which is already in its correct position and then decrease the length of heap by one.
- Repeat the step 2, until all the elements are in their correct position.

## Implementation

```c
void heap_sort(int Arr[]){
  int heap_size = N;

  build_maxheap(Arr);
  for (int i = N; i >= 2; i--) {
    swap | (Arr[1], Arr[i]);
    heap_size = heap_size - 1;
    max_heapify(Arr, 1, heap_size);
  }
}
```

**Complexity:** max_heapify has complexity O(log(N)), build_maxheap has complexity O(N) and we run max_heapify N-1 times in heap_sort function, therefore complexity of heap_sort function is O(N \* log(N)).
