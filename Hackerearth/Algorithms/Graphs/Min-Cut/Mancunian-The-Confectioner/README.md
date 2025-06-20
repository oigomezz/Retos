# [Mancunian, The Confectioner][link]

Mancunian wants to open his very own bakery in the city. Being an apprentice of the famous SAF who was known for his exquisite cake recipes, the residents of the city have similar high expectations from him.
There are M types of ingredients from which cakes are made, each of which has a cost. Each cake needs some number of these ingredients, not necessarily all of them. Initially, Mancunian has no ingredient present at his shop. He needs to buy the ones he needs. Once he buys some ingredient, he has access to an unlimited supply of it and does not need to ever buy it again.

At the grand opening of his bakery, Mancunian received orders from N customers, along with the price the customer is willing to pay for their ordered cake. Mancunian must decide to bake some of these cakes (not necessarily all) so that he can maximise his earnings. His earnings will be the money he earns from the sale of the cakes he bakes minus the cost of the ingredients he bought. Note that he may choose not to bake any cake.

Given a set of M ingredients available and a set of N cake orders, help Mancunian find the maximum amount he can earn.

## Input format

- The first line contains two integers N and M denoting the number of cake orders and ingredients respectively.
- The second line contains N integers denoting the selling prices of the cakes.
- The third line contains M integers denoting the costs of the ingredients.
- The next N lines contain M integers each. The jth integer in the i-th line is 1 if the i-th cake needs the jth ingredient and 0 otherwise.

## Output format

Output a single integer which is the answer to the problem.

[link]: https://www.hackerearth.com/practice/algorithms/graphs/min-cut/practice-problems/algorithm/mancunian-the-confectioner/
