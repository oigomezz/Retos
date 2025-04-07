# [DreamGrid's Luxury Shopping][link]

DreamGrid recently went on a shopping spree for luxury items at an exclusive boutique. In this boutique, there were n distinct items to choose from. DreamGrid, known for his ample wealth, employed an interesting shopping strategy:

- He meticulously inspected all n items in the store, starting from the 1-st item and ending with the n-th item.
- Whenever he checked an item, he only made a purchase if he had enough funds to cover its price. If his available funds were sufficient, he bought the item and subtracted its cost from his total wealth.
- If, at any point, his remaining funds were insufficient to buy the item being considered, he would simply skip that particular item.

Your task is to determine the maximum possible amount of wealth DreamGrid had at the beginning such that he can acquire some of these luxury items. You are provided with the prices of the n items and the total number of items DreamGrid ultimately purchased (indicated as m).

Your objective is to find out DreamGrid's maximum wealth that DreamGrid has before this extravagant shopping spree such that he can purchase m luxury items, which will be a non-negative whole number.

## Input format

- The first line consists of two integers n and m, separated by a space. Here,n denotes the total number of luxury items available in the boutique, and m represents the number of items DreamGrid eventually purchased.
- The next n lines each contains one integer pricei indicates the price of the i-th luxury item.

## Output format

Print the maximum amount of money DreamGrid needs to purchase m items in a new line.

[link]: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/dreamgrids-luxury-shopping-07b2f274/
