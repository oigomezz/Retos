# Bela Jornada

BR-101 (also called Translitorânea, officially named Rodovia Governador Mário Covas) is a longitudinal road in Brazil. It is the longest in the country.

The road has N checkpoints. Each checkpoint has a beauty value denoted as an array A in order from the start of the road to the end of the road. The beauty value of a checkpoint consists of the beauty of the places near the checkpoint. You are planning to travel along the road. Since it is a long road, you will stop at one of the checkpoints for a little rest and after that, continue your journey.

So, your journey in two nearby sub-arrays, S1 being the checkpoints before your rest (including the one you will stop at) and S2 being the checkpoints after your rest, such that size(S1) + size(S2) = N (i.e. every checkpoint belongs to an exact sub-array).

The total beauty of the journey is defined by sum(S1) \* sum(S2) where sum(S) is the total sum of beauty value in sub-array S. You want to maximize the value of sum(S1) \* sum(S2).

## Input format

The first line of input contains an integer N, denoting the number of checkpoints. The second line contains N separate integers, denoting the beauty value of the checkpoints.

## Output format

You have to present the maximum value of sum(S1) \* sum(S2).
