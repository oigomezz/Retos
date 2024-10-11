# Seating Arrangement

There are N chairs arranged in a row. K people come in a line and start occupying the chairs. Each person wants to be as far as possible from every other person. So, every person arriving looks for the largest empty continuous sequence of unoccupied chairs and occupies the middle position. They have a preference indicating whether they would choose the left or the right chair if there are two chairs at the middle to chose from (else the preference does not matter, since there is only 1 chair at the center). If there are multiple largest empty sequences, then the person chooses the sequence which appears first from left side. You are asked to answer Q queries. Determine which person has occupied the queried position.

## Input format

- The first line of every test file are 2 integers N and K.
- The next line contains a string S of length K. The ith character would be 'L' or 'R' indicating the preference of the ith person - the left or the right seat respectively.
- Next line contains an integer Q - the number of queries.
- Next Q lines contain an integer Qi - the queried position.

## Output format

For each query, output the persons' entry number if it is occupied, else print '-1' without quotes in a new line.
