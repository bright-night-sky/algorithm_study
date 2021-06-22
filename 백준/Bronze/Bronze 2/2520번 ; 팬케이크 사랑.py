# https://www.acmicpc.net/problem/2520

from sys import stdin


test_case = int(stdin.readline())

for test_case_idx in range(test_case):
    cm, y, ssu, ssa, f = map(int, stdin.readline().split(' '))
    b, gs, gc, w = map(int, stdin.readline().split(' '))