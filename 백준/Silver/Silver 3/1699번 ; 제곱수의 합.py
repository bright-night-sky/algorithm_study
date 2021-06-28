# https://www.acmicpc.net/problem/1699

from sys import stdin
from math import sqrt


N = int(stdin.readline())
term_cnt = 0

while N != 0:
    max_square_num = int(sqrt(N))
    N -= max_square_num ** 2
    term_cnt += 1

print(term_cnt)