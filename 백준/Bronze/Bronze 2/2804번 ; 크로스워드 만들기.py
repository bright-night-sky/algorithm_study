# https://www.acmicpc.net/problem/2804

from sys import stdin


A, B = stdin.readline().rstrip().split(' ')
A_len = len(A)
B_len = len(B)
cross_idx = 0

for B_char in B:
    if B_char in A:
        cross_idx = A.find(B_char)

