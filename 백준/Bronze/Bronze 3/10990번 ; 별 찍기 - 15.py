# https://www.acmicpc.net/problem/10990

from sys import stdin


N = int(stdin.readline())

for i in range(N):
    print(' ' * i, end='')
    print('*', end='')
    print(' ' * (2 * i - 1), end='')
    print('*')