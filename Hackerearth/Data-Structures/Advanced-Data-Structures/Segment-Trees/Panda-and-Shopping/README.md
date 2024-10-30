# Panda and Shopping

Panda loves to shop! And well, anyone who loves to shop gets a huge amount of happiness even after a tiring session of window shopping.

There are N shops, all aligned linearly having index 1,2,...,N. Buying any positive number of items from a shop Si gives a happiness equal to Hi. Unfortunately due to some unavoidable circumstances, every shop owner has introduced a value Li. You are credited Hi happiness from the i-th shop if and only if this is the first shop you are buying something from or you buy atleast one item from this shop and the last shop you shopped from was Sj such that Lj <= Li and j < i. Find the maximum sum of happiness that can be obtained following the rules given above!

## Input format

The first line contains N , the number of shops in the area. Each of the next N lines contains two space separated integers, Hi and Li, which denotes the values for the i-th shop (defined in the problem statement).

## Output format

Output consists of one line, which contains the maximum sum of happiness that can be obtained!
