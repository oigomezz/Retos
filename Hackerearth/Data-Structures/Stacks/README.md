# TUTORIAL

Stacks are dynamic data structures that follow the Last In First Out (LIFO) principle. The last item to be inserted into a stack is the first one to be deleted from it.

For example, you have a stack of trays on a table. The tray at the top of the stack is the first item to be moved if you require a tray from that stack.

## Inserting and deleting elements

Stacks have restrictions on the insertion and deletion of elements. Elements can be inserted or deleted only from one end of the stack i.e. from the top. The element at the top is called the top element. The operations of inserting and deleting elements are called push() and pop() respectively.

When the top element of a stack is deleted, if the stack remains non-empty, then the element just below the previous top element becomes the new top element of the stack.

For example, in the stack of trays, if you take the tray on the top and do not replace it, then the second tray automatically becomes the top element (tray) of that stack.

## Features of stacks

- Dynamic data structures
- Do not have a fixed size
- Do not consume a fixed amount of memory
- Size of stack changes with each push() and pop() operation. Each push() and pop() operation increases and decreases the size of the stack by 1, respectively.

## Operations

**push( x ):** Insert element x at the top of a stack

```C
void push (int stack[ ] , int x , int n) {
 if ( top == n-1 ) {         //If the top position is the last of position in a stack, this means that the stack is full
    cout << “Stack is full.Overflow condition!” ;
    }
    else{
        top = top +1 ;            //Incrementing top position
        stack[ top ] = x ;       //Inserting element on incremented position
    }
}
```

**pop( ):** Removes an element from the top of a stack

```C
void pop (int stack[ ] ,int n )
    {

        if( isEmpty ( ) )
        {
            cout << “Stack is empty. Underflow condition! ” << endl ;
        }
        else
        {
             top = top - 1 ; //Decrementing top’s position will detach last element from stack
        }
    }
```

**topElement ( ):** Access the top element of a stack

```C
int topElement ( )
    {
        return stack[ top ];
    }
```

**isEmpty ( ) :** Check whether a stack is empty

```C
bool isEmpty ( )
    {
        if ( top == -1 )  //Stack is empty
        return true ;
        else
        return false;
    }
```

**size ( ):** Determines the current size of a stack

```C
int size ( )
    {
        return top + 1;
    }
```

## Processing 2D arrays

The most basic form of processing is to loop over the array and print all its elements, which can be done as follows:

```C
type arr[row_size][column_size] = {{elements}, {elements} ... }
for i from 0 to row_size
    for j from 0 to column_size
        print arr[i][j]
```

These methods of declaration, initialization, and processing can be extended to 3D or higher dimensional arrays.
