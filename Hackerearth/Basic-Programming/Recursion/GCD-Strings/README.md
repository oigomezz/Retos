# GCD Strings

Let P[0 ... N-1] be a binary string of length N. Then let's define S∞(P) as an infinite string with S∞[i] = P[i%N] ∀i >= 0 (informally, S∞(P) is the concatenation of P with itself an infinite number of times).

Define the GCD-string of two integers a,b with a >= b to be a binary string of length a that satisfies the following:

- g(a,b) = 100...000 (1 followed by a-1 zeros) if a is divisible by b.
- g(a,b) = First a characters of S∞(g(b,a mod b)) otherwise.

We can define F(a,b) to be the value of the integer represented by the binary string g(a,b) in base-2. Given T pairs of integers (x,y), compute F(a,b) mod 10⁹ + 7 for each pair.

## Input format

- The first line will contain the number of test cases T.
- Each test case can be described with a single line containing two integers x,y.

## Output format

Print the answer to each test case in a new line.
