# [Array revolve][link]

You are given an array A(1-based index) consisting of N integers. You have to process two types of queries on this array.

- **Type 1:** Given ID and VAL, perform the operation UPDATE(ID, VAL)

      UPDATE(ID, VAL):
        if VAL == 0:
            return

        AID = AID + VAL

        if ID == N:
            UPDATE(1, VAL - 1)
        else :
            UPDATE(ID + 1, VAL - 1)

- Type 2: Given L and R, find QUERY(L, R)

      QUERY(L, R):
        if L == R:
            return AL

        if L == N:
            return AL + QUERY(1, R)
        else :
            return AL + QUERY(L + 1, R)

## Input format

- The first line of input contains two space separated integer N and Q denoting size of array and number of queries respectively.
- The second line contains N space separated integers denoting array A.
- Next Q lines are of one of the following format:
  - 1 ID VAL : for type 1 query
  - 2 L R : for type 2 query

## Output format

For each type 2 query, output the answer modulo 10⁹ + 7 in a new line.

[link]: https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/bob-and-string-easy/
