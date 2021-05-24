# https://www.acmicpc.net/problem/1934
import math
from sys import stdin
from math import lcm

T = int(stdin.readline())

for test_case_idx in range(T):
    A, B = map(int, stdin.readline().split(' '))

    print(lcm(A, B))