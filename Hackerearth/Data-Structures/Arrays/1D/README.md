# TUTORIAL

An array is a sequential collection of elements of same data type and stores data elements in a continuous memory location. The elements of an array are accessed by using an index. The index of an array of size N can range from 0 to N-1. For example, if your array size is 5, then your index will range from 0 to 4 (5-1). Each element of an array can be accessed by using arr[index].

## Array declaration

Declaring an array is language-specific.

For example, in C/C++, to declare an array, you must specify, the following:

- Size of the array: This defines the number of elements that can be stored in the array.
- Type of array: This defines the type of each element i.e. number, character, or any other data type.

A C++ example would be:

```C++
int arr[5];
```

This is a static array and the other kind is dynamic array, where type is just enough for declaration. In dynamic arrays, size increases as more elements are added to the array.

## Array Initialization

Array can be initialized either at the time of declaration or after that.

The sample format if an array is initialized at the time of declaration is

```C++
type arr[size] = {elements}
```

The sample format of an array that is initialized in C++, is

```C++
int arr[5] = {4, 12, 7, 15, 9};
```

An array can be initialized after declaration by assigning values to each index of the array as follows

```C++
type arr[size]
 arr[index] = 12
```

## Processing an Array

The most basic form of processing an array is to loop over the array and print all its elements.

A sample of processing an array by looping over the array and printing its elements is as follows:

```C++
type arr[size] = {elements}
for idx from 0 to size
    print arr[idx]
```
