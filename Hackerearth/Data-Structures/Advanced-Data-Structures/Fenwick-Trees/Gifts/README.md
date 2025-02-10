# Gifts

This festive Season HackerEarth decided to send gifts to all of its contributors. Xsquare , Sentinel , Subway , darkshadows and Venomous got their favourite gifts i.e ,an array full of integers. Contrary to that ma5termind got his favourite string str consisting of upper case letters 'A' , 'B' , 'C' , 'D' and 'E' only. To avoid any kind of comparison ,all the gifts are of same size i.e N. As HackerEarth promotes a very friendly culture, all of them have decided to play together with these gifts. For the purpose to serve ...

1. Xsquare named his array as A.
2. Sentinel named his array as B.
3. Subway named his array as C.
4. Darkshadows named his array as D.
5. Venomous named his array as E.

They will mainly perform three types of task.

Qe X Y : X and Y are the characters denoting the initials of the array.

    def func_Qe(X,Y):
        for i in range(1,N+1):        #[1,N] (considering 1 based indexing)
            temp = X[i]
            X[i] = Y[i]
            Y[i] = temp
        return

Qc x Y : x is an interger denoting an index in the string and Y is a character.

    def func_Qc(x,Y):
        str[x] = Y
        return

Qs x y : x and y are the integers denoting the xth and yth indices in the string such that x <= y.

    def func_Qs(x,y):
        sum = 0
        for i in range(x,y+1):
            sum = sum + (select str[i] as array name and add ith element of this array)
        return sum

refer to the sample test case for better explanation of the problem.

Although they love this game, but all of them have to go to a party tonight. So,they want to finish this game as soon as possible.

## Input format

- First line of input contains a single integer N denoting the size of each gift.
- Next line of input contains N space separated integers denoting the array A.
- Next line of input contains N space separated integers denoting the array B.
- Next line of input contains N space separated integers denoting the array C.
- Next line of input contains N space separated integers denoting the array D.
- Next line of input contains N space separated integers denoting the array E.
- Next line of input contains a string str denoting ma5termind's string.
- Next line of input contain a single integer Q denoting the number of tasks to be preformed.
- Next Q line of input contains Q tasks, each from any of the 3 mentioned types.

## Output format

Output consists of several lines. For each task of type Qs, print the required answer.
