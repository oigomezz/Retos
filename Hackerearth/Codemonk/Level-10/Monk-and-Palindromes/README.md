# Monk and Palindromes

Monk loves maths and is always curious to learn new things. Recently, he learned about palindromes. Now, he decided to give his students a problem which uses maths and the concept of palindromes. So, he wants the students to find how many different numbers they can create according to the following conditions. He will give the students an integer N which will denote the total number of digits in the final number. Also he will provide them with Q conditions where these conditions will be of form A B where the number formed by concatenating the digits from the A-th position to B-th position is a palindrome. You can learn more about palindromes here.

**Note:** Numbers with leading zeros are also to be considered.

## Input format

- First line consists of the integer N denoting the number of digits in final number.
- Next line consists of the integer Q denoting the number of conditions.
- Next Q lines will be of the form A B which denotes that the number formed by concatenating the digits from the A-th position to B-th position of the final number is a palindrome.

## Output format

Print the number of different numbers the students can create by following the conditions. Since the answer can be very large, print it modulo 10⁹ + 7.
