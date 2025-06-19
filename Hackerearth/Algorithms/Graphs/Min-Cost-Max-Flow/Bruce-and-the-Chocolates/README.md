# [Bruce and the Chocolates][link]

Early this morning, I found our little Bruce sitting on a bench alone in the park. I sat beside him to ask where has he dropped his smile this morning?

Bruce: "Oh, Hi.. I love chocolates. (Who doesn't? ). It's chocolate day in school, and I forgot! Everyone is bringing chocolates. We play a game on this day, where the teacher makes pair of students and the students in each pair share their chocolates. I will have to go empty handed and hence, won't get paired :( "

"That's okay ,Bruce. You can ask your friends to share with you"

Bruce: " I did a smarter thing, I talked to my Mathematics teacher. I'm her favorite! She agreed that I could do the pairing! and from every pair , I could take 'x' number of chocolates, where x is the greatest number of chocolates that divides the number of chocolates with both the students. Now, I don't know how do I pair them! Not everyone can be paired with everyone, friendship issues. Can you help me out?"

You are given the number of chocolates with each student and all the possible pairs of the form (i,j) where ith and jth student can be paired. Help Bruce pair the students, so as to maximize the number of chocolates he can have .

You may assume:

- No pairs should overlap. No student is left alone (except Bruce).
- Total number of students in class is always odd.
- No one is absent on the Chocolate Day!
- For a possible pairing (i,j) , ( i+j ) mod 2 > 0.

## Input format

- First line of the input contains T (1<=T<=10) denoting the number of test cases. T testcases follow.
- For each test case, the first line contains two space-separated integers 'n' (1<=n<200) and 'm' (m>=0) , the total number of students in the class and the number of possible pairings.
- Next line contains 'n-1' integers, where Ai (1<=Ai<=10000) is the number of chocolates with the i'th student.
- The following m lines contain the description of possible pairs. The k-th line contains two space-separated integers Ik, Jk (1<=Ik,Jk<=n-1 ) .

## Output format

Output the maximum number of chocolates that Bruce can have.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/minimum-cost-maximum-flow/practice-problems/algorithm/bruce-and-the-chocolates-9/
