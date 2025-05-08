# [Split the Bill][link]

In the Splitwise app, people form groups and add the expenses of members of the group. This is especially useful for vacations, where people traveling in a group can maintain an account of their expenses and who paid the bills.

All people in the group are assigned distinct IDs between 1 and N, where N is the size of the group.

In addition to keeping a record of the expenditure, Splitwise also calculates the list of shortest-path transfers (defined later) that will settle up all dues.

Each transaction has the following parameters:

- transaction_id - It is a string representing the unique ID by which the transaction is identified.
- paid_by - It is a list of lists, where each element of the list is another list having the form [x, y]. Here, x and y denote that person having ID x paid Rs. y.
- split_as - It is a list of lists, where each element of the list is another list having the form [x, y]. Here, x and y denote that after all dues are settled, a person having ID x will ultimately contribute Rs. y to the transaction.

For any given transaction, the following condition holds true:

    Total_amount_paid = Sum_of_all_splits

In other words, the sum total of all amounts in list paid_by equals the sum total of all amounts in list split_as.

**Shortest-Path Transfers:** Shortest-path transfers lead to a reduction in the number of transfers.

Specifically, for a group having multiple transactions, the shortest-path transfers will be a list of payments to be made such that:-

- Each payment can be represented by a list of the following form:- [payer_id, payee_id, amount]. There is only 1 payer, and 1 payee in each payment, which are distinct from each other. So, payer_id != payee_id, for any payment.
- Each person (out of the N people) can only either be the payer (in all payments involving him), or the payee, but not both.
- The total amount of money that each person should receive/spend, must be equal to the total amount he would receive/spend according to the given list of transactions.

Clearly, there can be several shortest-path transfers for a particular list of transactions.

Specifically, the lexicographically smallest shortest path has the following:-

- Arrange people who have borrowed money in ascending order of their IDs. Do the same for people who have lent money.
- Now, construct payments so that the least borrower ID has to pay the least lender ID. Continue this process, till all debts have been settled.

**Task** Given N members in a group, and lists representing the transactions(expenses), print the payments involved in the lexicographically smallest shortest-path transfers for the group.

**Function description** Complete the function solve provided in the editor. This function takes the following 2 parameters and returns the required answer:

- N: An integer, representing the number of people in the group.
- transaction_list: A list (vector) of transactions. Each transaction is a dictionary, having keys “transaction_id”, “paid_by” and “split_as”. (The contents of each transaction are explained above)

## Input format

**Note:** This is the input format that you must use to provide custom input (available above the Compile and Test button).

- The first line contains two space-separated integers N and M, the number of people in the group, and the number of transactions recorded.
- The next lines describe the M transactions as follows:
  - Each new transaction begins from a new line.
  - The first line of each transaction contains a string, representing the transaction_id of the transaction.
  - The 2nd line of each transaction contains 2 space-separated integers n_payers and n_splits.
  - n_payers denotes the number of people in the paid_by list. n_splits denotes the number of people in the split_as list.
  - The next n_payers lines contain two space-separated integers, the payer and the amount paid.
  - The next n_splits lines contain two space-separated integers, the borrower and the amount borrowed.

## Output format

Print the answer in the given format.

- In the first line, print a single integer K, denoting the number of payments involved in the Shortest Path Transfer.
- The next K lines should represent the K payments. Each payment should be printed in a single line as 3 space-separated integers payer_id, payee_id, and amount. Here, payer_id is the ID of the person who needs to pay the amount of money to the person with ID payee_id.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/split-the-bill-3-5a0690ff/
