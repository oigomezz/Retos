# [Special Sum][link]

Special Sum of number N is defined as follows:

```python
def foo(n):
    ret = 0
    for i in range(1, n + 1):
        if gcd(n, i) is 1:
            ret += 1
    return ret
```

```python
def SpecialSum(N):
    ret = 0
    for i in range(1, N + 1):
        if i divides N:
            ret += foo(i)
    return ret
```

Given a N print SpecialSum(N).

## Input format

- First line contains T, the number of testcases.
- Each testcase consists of one line containing N.

## Output format

Print in one line for each testcase the required answer.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/special-sum-3/
