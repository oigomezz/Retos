# TUTORIAL

Binary Indexed Tree also called Fenwick Tree provides a way to represent an array of numbers in an array, allowing prefix sums to be calculated efficiently. For example, an array [2, 3, -1, 0, 6] is given, then the prefix sum of first 3 elements [2, 3, -1] is 2 + 3 + -1 = 4. Calculating prefix sum efficiently is useful in various scenarios. Let's start with a simple problem.

Given an array A[], and two types of operations are to be performed on it.

1. Change the value stored at an index i. (This is called a point update operation)
2. Find the sum of a prefix of length k. (This is called a range sum query)

A straightforward implementation of the above would look like this.

```C
int a[] = {2, 1, 4, 6, -1, 5, -32, 0, 1};
void update(int i, int v)   // assigns value v to a[i]
{
    a[i] = v;
}
int prefixsum(int k)    // calculate the sum of all a[i] such that 0 <= i < k
{
   int sum = 0;
   for(int i = 0; i < k; i++)
        sum += a[i];
   return sum;
}
```

This is a perfect solution, but unfortunately, the time required to calculate a prefix sum is proportional to the length of the array, so this will usually time out when large numbers of such intermingled operations are performed.

One efficient solution is to use segment tree that can perform both operations in O(logN) time.

Using binary Indexed tree also, we can perform both the tasks in O(logN) time. But then why to learn another data structure when segment tree can do the work for us. It’s because binary indexed trees require less space and are very easy to implement during programming contests (the total code is not more than 8-10 lines).

Before starting with the binary indexed tree, have a look at a particular bit manipulation trick.

## Basic Idea of Binary Indexed Tree

We know the fact that each integer can be represented as the sum of powers of two. Similarly, for a given array of size N, we can maintain an array BIT[] such that, at any index we can store the sum of some numbers of the given array. This can also be called a partial sum tree.

Let’s use an example to understand how BIT[] stores partial sums.

```C
//for ease, we make sure our given array is 1-based indexed
int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
```

![example](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

The above picture shows the binary indexed tree, each enclosed box of which denotes the value BIT[index] and each BIT[index] stores partial sum of some numbers.

To generalize this every index i in the BIT[] array stores the cumulative sum from the index i to i - (1 << r) + 1 (both inclusive), where r represents the last set bit in the index i.

Sum of first 12 numbers in array A[] = BIT[12] + BIT[8] = (A[12] + ... + A[9]) + (A[8] + ... + A[1])

Similarly, sum of first 6 elements = BIT[6] + BIT[4] = (A[6] + A[5]) + (A[4] + ... + A[1])

Sum of first 8 elements = BIT[8] = (A[8] + ... + A[1])

Let’s see how to construct this tree and then we will come back to querying the tree for prefix sums. BIT[] is an array of size = 1 + the size of the given array on which we need to perform operations. Initially all values in BIT[] are equal to 0. Then we call update() operation for each element of given array to construct the Binary Indexed Tree. The update() operation is discussed below.

```C
void update(int x, int val)       //add "val" at index "x"
{
    for(; x <= n; x += x&-x)
          BIT[x] += val;
}
```

If we look at the for loop in update() operation, we can see that the loop runs at most the number of bits in index x which is restricted to be less or equal to N(the size of the given array), so we can say that the update operation takes at most O(logN) time.

How to query such structure for prefix sums? Let’s look at the query operation.

```C
int query(int x)      //returns the sum of first x elements in given array a[]
{
     int sum = 0;
     for(; x > 0; x -= x&-x)
         sum += BIT[x];
     return sum;
}
```

## When to use Binary Indexed Tree?

Before going for Binary Indexed tree to perform operations over range, one must confirm that the operation or the function is:

Associative. i.e f(f(a,b),c) = f(a,f(b,c)) this is true even for seg-tree

Has an inverse. eg:

1. Addition has inverse subtraction (this example we have discussed).
2. Multiplication has inverse division.
3. GCD() has no inverse, so we can’t use BIT to calculate range gcd’s.
4. Sum of matrices has inverse.
5. Product of matrices would have inverse if it is given that matrices are degenerate i.e. determinant of any matrix is not equal to 0.

**Space Complexity:** O(N) for declaring another array of size N.

**Time Complexity:** O(logN) for each operation(update and query as well).

## Applications

1. Binary Indexed trees are used to implement the arithmetic coding algorithm. Development of operations it supports were primarily motivated by use in that case.
2. Binary Indexed Tree can be used to count inversions in an array in O(N logN) time.
