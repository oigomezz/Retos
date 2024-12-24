# [Exception Handling][link]

You are given a piece of Java code. You have to complete the code by writing down the handlers for exceptions thrown by the code. The exceptions the code may throw along with the handler message are listed below:

Division by zero: Print "Invalid division".
String parsed to a numeric variable : Print "Format mismatch".
Accessing an invalid index in string : Print "Index is invalid".
Accessing an invalid index in array : Print "Array index is invalid".

MyException : This is a user defined Exception which you need to create. It takes a parameter param. When an exception of this class is encountered, the handler should print "MyException[param]", here param is the parameter passed to the exception class.

Exceptions other than mentioned above : Any other exception except the above ones fall in this category. Print "Exception encountered".

Finally, after the exception is handled, print "Exception Handling Completed".

Example: For an exception of MyException class if the parameter value is 5, the message will look like
MyException[5].

## Input format

The code handles all the input itself.

## Output format

If any exception is encountered in the code, print the respective handler code.
The last line of output should be "Exception Handling Completed".

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/exception-handling-2-46f67551/
