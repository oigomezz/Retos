# [Prateek and theories][link]

Scientists, researchers, mathematicians and thinkers propose theories for a number of things. For explaining a single thing, a number of theories are proposed. A number of theories are rendered invalid after a new and more relevant theory surfaces, giving a better and a more valid explanation for the subject of the theory. For this problem, we are only concerned with one field of study, lets say, A. In the field A, a number of theories were proposed for a number of domains in the field.

For a particular theory, the time at which it was proposed be T1 and the time at which it becomes invalid be T2. We define the theory period for this particular theory as [T1, T2). Both T1 and T2 are recorded in seconds from some reference point, B. We are given the theory periods for a number of theories. It is possible that more than one theory in the field A might be valid at some second, T (Recorded with reference to B ). Let us call the value of the number of valid theories at the second T as popularity of the field at second T. The popularity of the field would be maximum at some point in time. Your task is simple, that is calculate this maximum value of popularity for the field A.

## Input format

- The first line of the input contains the integer t , the number of test cases.
- For each test case first line contains a positive integer n , that is, the number of theories.
- Then, n lines follow, one for each theory(1 to n ). Each line contains, 2 integers T1[i] and T2[i].
- T1[i] is the lower bound of the theory period for the theory i. (1 <= i <= n )
- T2[i] is the upper bound of the theory period for the theory i. (1 <= i <= n )

## Output format

The output contains t lines, one for each test case. Each line contains a positive integer, the required answer for that test case.

[link]: https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/prateek-and-theories-3/
