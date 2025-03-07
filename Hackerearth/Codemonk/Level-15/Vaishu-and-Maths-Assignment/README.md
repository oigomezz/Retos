# Vaishu and Maths Assignment

Vaishu's teacher had written some positive integers on blackboard with corresponding operations to perform with them.

So, student should start from 0 and keep on doing operations with the given integers in the same order as they were written on the board, to get a final result. The operations only consisted of addition and subtraction. Vaishu was little slow in calculating and the class got over soon. As, she could not complete the calculation, she will do the remaining part as an assignment. So, she noted the result L where she stopped. But unfortunately, she could only note down the next list of integers and forgot to write down their corresponding operation, that is either to add or subtract them with the previous obtained result. To make sure, that the students don't deviate too much, teacher had told them that answer at any point won't exceed Y and won't fall below X.

Now, this has increased Vaishu's effort even more. She will be preparing multiple assignments, with every possible scenario but keeping in mind that result is always between X and Y (both inclusive).

Her one of the close friend is ready to help, but he will only be verifying her results and not doing assignments on her behalf. So, he starts asking her queries of the following two types.

- '>'M : Is the final result in any assignment greater than M ?
- '<'M: Is the final result in any assignment lesser than M ?

Vaishu will be answering his queries by looking at all the assignments in the following way:

- YES: If there is even a single assignment where result is greater or lesser than M depending on query type with restriction that result after applying every operation should be between X and Y.
- NO: If there is not even a single assignment where result is greater or lesser than M depending on query type and restriction that result after applying every operation should be between X and Y.

## Input format

- First line of the input contains four single space separated integers L,N,X and Y denoting the Vaishu's result when class got over, count of left out positive integers that she wrote hurriedly for her assignment, minimum and maximum limit of every result given by her teacher respectively.
- Next line contains N single space separated integers denoting the numbers she noted down from blackboard but forgot to wrote down the corresponding operations for the same.
- Next line contains an integer Q denoting the number of queries asked by her friend.
- Each of the Q lines will contain queries of type A B, where A is either '>' or '<' (without quotes) and B is the number been put by her friend for verifying her results.

## Output format

For each query been asked, print out one of the two possible replies : 'YES' or 'NO' (without quotes) depending on the query asked by Vaishu's friend.
