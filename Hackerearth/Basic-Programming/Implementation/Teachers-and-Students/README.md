# [Teachers and Students][link]

There are N students in a class and each student has a number denoted by an array A. The teacher will select three students and give a task to each of them. The first student has to find a number of subsets of students having cumulative xor less than K. The second student has to find a number of subsets of students having cumulative xor equal to K. The third student has to find a number of subsets of students having cumulative xor greater than K. Let the three numbers returned by the selected students are cnt1, cnt2 and cnt3. You need to find the value of :

(cnt1 + cnt2)^2 + (cnt2 + cnt3)^2 + (cnt3 + cnt1)^2 - (cnt1^2 + cnt2^2 + cnt3^2)

## Input format

- The first line contains an integer T denoting the number of test cases.
- The first 2 lines of each test case have 2 integers N and K respectively.
- Next line has N integers denoting the array A.

## Output format

Print answer for each test case under modulo 10^9 + 7 in a new line.

[link]: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/another-xor-problem-1-8f7f54e8/
