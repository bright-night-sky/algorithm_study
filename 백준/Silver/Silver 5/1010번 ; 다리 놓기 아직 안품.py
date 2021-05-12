# https://www.acmicpc.net/problem/1010

from sys import stdin
from itertools import permutations

T = int(stdin.readline().rstrip())

cases_cnt = 1

for test_case_idx in range(T):
    N, M = map(int, stdin.readline().rstrip().split(' '))

    for num in range(M, M - N, -1):
        print(num)
        cases_cnt *= num

    print(int(cases_cnt))