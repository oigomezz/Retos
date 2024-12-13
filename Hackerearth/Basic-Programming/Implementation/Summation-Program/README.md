# [Summation Program][link]

You are given a number N. You are required to determine the value of the following function:

```C++
long long int solve(N)
{
    ans=0;
    for(i=1;i<=N;i++)
    ans+=(N/i);
    return ans;
}
```

All divisions are integer divisions(i.e. N/i is actually floor(N/i)).

## Input format

- First line: T denoting the number of test cases.
- Each of the next T lines: An integer N.

## Output format

For each test case, print the answer in a new line.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/floor-sum-45e7b417/
