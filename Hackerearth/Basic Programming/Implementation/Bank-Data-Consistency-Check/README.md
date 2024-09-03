# Bank Data Consistency Check

Bank X contains a database of account numbers and debit cards mapped to each other. Now due to some technical issues, the data suddenly got deleted. But now the bank is left with a list of pair of integers but they don’t know which of them is the debit card no. and which one is the account number.

It is clear that an account can have multiple debit cards linked to it, but it is not possible that a debit card is linked to more than one accounts.

You need to check if the given data is recoverable or not. If it is consistent then you need to also find what is the account number and what is the debit card number. It is guaranteed that the input data is designed in a way that there is only one unique correct answer.
If for a pair it is impossible to find, you need to print -1 -1.

**Note:**

- The input data contains a pair of integers and you have to decide for each pair, which is the account number and which is the debit card.
- The account number can be of any length and debit card no can also be of any length. It is possible that the same pair of the integer is repeated more than once in the data.
- The data is just dummy and is built up only for the competition purpose.

## Input format

There are several lines of input, each line having a pair of integers. You need to write the code such that it reads until the input data ends. The input ends with the pair -1 -1 and you don't need to calculate the result for it.

## Output format

For each line of the output, you need to print 0 corresponding to the number which is account number and 1 corresponding to the debit card number. If there is a pair for which it is not possible to confirm if its a debit card no. or the bank account number print "-1 -1" without quotes.
