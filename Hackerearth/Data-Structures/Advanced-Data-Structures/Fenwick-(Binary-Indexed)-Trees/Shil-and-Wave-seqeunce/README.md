# Shil and Wave seqeunce

Given a sequence A1 , A2 , A3 .. AN of length N . Find total number of wave subsequences having length greater than 1.

Wave subsequence of sequence A1 , A2 , A3 .. AN is defined as a set of integers i1 , i2 .. ik such that Ai1 < Ai2 > Ai3 < Ai4 .... or Ai1 > Ai2 < Ai3 > Ai4 .... and i1 < i2 < ...< ik.Two subsequences i1 , i2 .. ik and j1 , j2 .. jm are considered different if k != m or there exists some index l such that il ! = jl.

## Input format

- First line of input consists of integer N denoting total length of sequence.
- Next line consists of N integers A1, A2, A3, ..., AN.

## Output format

Output total number of wave subsequences of given sequence . Since answer can be large, output it modulo 10⁹ + 7.
