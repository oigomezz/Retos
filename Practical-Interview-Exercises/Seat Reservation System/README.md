# Seat Reservation System

A movie theater has N seats numbered 1 to N. Build a seat reservation system that performs one of the following operations K times:

- Fetches the smallest-numbered unreserved seat then reserves It and retums its number.
- Cancels a seat reservation for seat [i]. The result should be an array containing the reserved seat numbers.

## Notes

- If seat[i]=0, reserve the seat.
- If seat [i]>0, cancel the reservation of a seat.
- Every time we reserve a seat, it is guaranteed that there is an unreserved seat.
- Every time we cancel the reservation of a seat, it is guaranteed

## Function description

The function takes the following 3 parameters and returns the solution:

- N. Represents the number of seats.
- K: Represents the number of operations.
- seat. Represents the details of operations.

## Input format for custom testing

Note: Use this input format if you are testing against custom input or writing code in a language where we don't provide boilerplate code

- The first line contains N denoting the number of seats.
- The second line contains K denoting the number of operations.
- The third line contains seat denoting the details of operations.

Input format

- 1 ≤ N ≤ 10^5
- 1 ≤ K ≤ 10^5
- 0 ≤ seat[i] ≤ N
