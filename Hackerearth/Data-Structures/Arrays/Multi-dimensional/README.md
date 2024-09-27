# TUTORIAL

A multi-dimensional array is an array of arrays. 2-dimensional arrays are the most commonly used. They are used to store data in a tabular manner.

Consider following 2D array. For an array of size N x M, the rows and columns are numbered from 0 to N-1 and columns are numbered from 0 to M-1, respectively. Any element of the array can be accessed by arr [i] [j] where 0 <= i < N and 0 <= j < M.

## 2D array declaration

To declare a 2D array, you must specify the following:

- Row-size: Defines the number of rows
- Column-size: Defines the number of columns
- Type of array: Defines the type of elements to be stored in the array i.e. either a number, character, or other such datatype. A sample form of declaration is as follows:

```C
type arr[row_size][column_size]
```

## 2D array initialization

An array can either be initialized during or after declaration. The format of initializing an array during declaration is as follows:

```C
type arr[row_size][column_size] = {{elements}, {elements} ... }
```

Initializing an array after declaration can be done by assigning values to each cell of 2D array, as follows.

```C
type arr[row_size][column_size]
arr[i][j] = 14
```

This is quite naive and not usually used. Instead, the array elements are read from STDIN.

## Processing 2D arrays

The most basic form of processing is to loop over the array and print all its elements, which can be done as follows:

```C
type arr[row_size][column_size] = {{elements}, {elements} ... }
for i from 0 to row_size
    for j from 0 to column_size
        print arr[i][j]
```

These methods of declaration, initialization, and processing can be extended to 3D or higher dimensional arrays.
