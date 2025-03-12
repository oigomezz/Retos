# [Attendance][link]

As per COVID-19 rules, your college is taking online classes. Your professor takes class from StartTime(hh:mm:ss) to EndTime(hh:mm:ss). He uses a chrome extension to track when a student joins the class and leaves the class with their Student ID(SID). He stores it in a student tracker file and then circulates it in your college group. Now, your teacher is very strict. He wants to take attendance at a moment when the number of students present in the class is minimum. If there are multiple such times he can choose a time with equal probability and will take the attendance. Now, you know your teacher's algorithm and you have access to the student tracker file.

## Task

Print 0 if the probability that you (SID=1) will get the attendance is zero otherwise print the probability in P/Q format where GCD(P, Q)=1, where GCD(P, Q) denotes the greatest common divisor of integers P and Q.

**Note:** Each student can join the class at multiple intervals. Like they can join at "12:00:00" then leave at "12:15:00", then again join at "12:35:00", and leave at "12:50:00".

## Input format

- The first line contains N denoting the number of students.
- The second line contains two space-separated strings StartTime and EndTime of class in hh:mm: ss format("00:00:00" to "23:59:59")
- The next N lines have Student ID(SID), the number of intervals the student joined the class(M), and M pairs of [ArrivalTime, LeaveTime] in hh:mm:ss format for each M interval.

## Output format

Print 0 if the probability that you (SID=1) will get the attendance is zero otherwise print the probability in P/Q format where GCD(P, Q)=1, where GCD(P, Q) denotes the greatest common divisor of integers P and Q.

[link]: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/attendance-72-5c241efb/
