# TUTORIAL

When a function calls itself, its called Recursion. It will be easier for those who have seen the movie Inception. Leonardo had a dream, in that dream he had another dream, in that dream he had yet another dream, and that goes on. So it's like there is a function called dreams(), and we are just calling it in itself.

    function dream()
      print "Dreaming"
      dream()

Recursion is useful in solving problems which can be broken down into smaller problems of the same kind. But when it comes to solving problems using Recursion there are several things to be taken care of. Let's take a simple example and try to understand those. Following is the pseudo code of finding factorial of a given number X using recursion.

    function factorial(x)
      if x is 0                    // base case
        return 1
      return x*factorial(x-1)       // break into smaller problem(s)

**Base Case:** Any recursive method must have a terminating condition. Terminating condition is one for which the answer is already known and we just need to return that. For example for the factorial problem, we know that factorial(0) = 1, so when x is 0 we simply return 1, otherwise we break into smaller problem i.e. find factorial of x-1. If we don't include a Base Case, the function will keep calling itself, and ultimately will result in stack overflow. For example, the dream() function given above has no base case. If you write a code for it in any language, it will give a runtime error.

Number of Recursive calls: There is an upper limit to the number of recursive calls that can be made. To prevent this make sure that your base case is reached before stack size limit exceeds.

So, if we want to solve a problem using recursion, then we need to make sure that:

- The problem can broken down into smaller problems of same type.
- Problem has some base case(s).
- Base case is reached before the stack size limit exceeds.

## Backtracking

So, while solving a problem using recursion, we break the given problem into smaller ones. Let's say we have a problem A and we divided it into three smaller problems B, C and D. Now it may be the case that the solution to A does not depend on all the three subproblems, in fact we don't even know on which one it depends.
Let's take a situation. Suppose you are standing in front of three tunnels, one of which is having a bag of gold at its end, but you don't know which one. So you'll try all three. First go in tunnel 1, if that is not the one, then come out of it, and go into tunnel 2, and again if that is not the one, come out of it and go into tunnel 3. So basically in backtracking we attempt solving a subproblem, and if we don't reach the desired solution, then undo whatever we did for solving that subproblem, and try solving another subproblem.
