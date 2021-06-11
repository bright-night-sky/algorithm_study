# https://www.acmicpc.net/problem/12033

from sys import stdin


T = int(stdin.readline())

for test_case_idx in range(T):
    N = int(stdin.readline())
    P = list(map(int, stdin.readline().split(' ')))
    y = ''

    for Pi in P:
        if int(Pi / 0.75) in P:
            y += str(Pi) + ' '
