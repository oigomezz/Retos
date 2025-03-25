# [Mobile Selection][link]

John has opened a new mobile shop. Each mobile is having following properties associated to it :

- Operating System ( Windows, Android or iOS)
- RAM Size (2, 4 or 8 GB)
- Memory Space (32 or 64 GB)
- Price
- Rating (based on other features like camera, touch quality, etc)

Now a customer comes to the store and tells his choice of Operating System, RAM size, Memory Space and his budget that he is willing to spend on the mobile. John will give the customer that mobile phone whose rating is maximum which also satisfies the criteria of Operating System, RAM size and Memory Space as specified by that customer and also whose price lies within the customer’s budget. If more than one eligible phone have maximum rating then, he can give any phone to the customer.

**Note:** All the queries are independent of each other.

**Hint:** Maintain a list of phone prices and rating for each combination of OS,RAM and Memory. For a given combination, find the one with best rating in given budget.

## Input format

- First line contains an integer N denoting number of mobile phones in John's shop.
- Each of the next N lines contains a string S followed by four integers A, B, C and D respectively where S denotes the operating system of the phone, A denotes the ram size of the phone, B denotes the memory space of the phone, C denotes the price of the phone and D denotes the rating of the phone.
- Next line contains an integer Q denoting the number of customers who have visited John's shop.
- Each of the next Q lines contains a string H followed by three integers E, F and G respectively where H denotes the choice of operating system of the phone required by the customer, E denotes the choice of ram size of the phone required by the customer, F denotes the choice of memory space of the phone required by the customer and G denotes the budget of the customer.

## Output format

For each query print the rating of the mobile phone given to customer by John as specified by the rules mentioned above. If there is no mobile phone available in John's shop following the customer's constraints, print 1. Answer for each query should be in new line.

[link]: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/mobile-selection-acc2cf2b/
