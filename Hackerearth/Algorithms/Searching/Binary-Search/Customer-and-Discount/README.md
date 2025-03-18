# [Customer and Discount][link]

You are given an array arr of length N, representing money with N customers. The i-th customer has arri rupees. There is another array cost of length M, representing the cost of M items in a store. The j-th item costs costj rupees. The store offers some discount money d which any customer can use to buy an item. Each customer can buy only one item and cannot use his money to buy an item for any other customer.

**Task:** Determine the maximum number of customers who can buy an item and the minimum total sum of customers’ money spent to achieve maximum customers with an item.

## Notes

- Assume 1-Based Indexing.
- The discount money d is common for all the customers, i.e., if one customer spends r rupees from d, then the discount money is reduced to (d-r) for all the customers.
- Multiple customers can spend money from the discount.

## Function Description

Complete the function maxCustomers provided in the editor. The function takes the following parameters and returns an array consisting of 2 integers, the maximum number of customers with items, and the minimum total customers' money spent:

- N: Represents the size of array arr
- M: Represents the size of array cost
- d: Represents the value of discount money
- arr: Represents the elements of array arr
- cost: Represents the elements of array cost

## Input format

**Note:** This is the input format you must use to provide custom input (available above the Compile and Test button).

- The first line of the input contains three integers N, M, and d, denoting the number of customers, the number of items, and the discount money.
- The second line of the input contains N integers arr1, arr2, …, arrN, where arri is the money with the i-th customer.
- The third line of the input contains M integers cost1, cost2, …, costM, where costj is the price of the j-th item.

## Output format

Print two space-separated numbers, the maximum number of customers who can buy an item and the minimum total customers' money needed for buying the maximum number of items.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/pirates-and-swords-89e51e63/
