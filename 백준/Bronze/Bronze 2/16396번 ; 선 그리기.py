# https://www.acmicpc.net/problem/16396

from sys import stdin


N = int(stdin.readline())
lines = tuple((0, 0))

for line_idx in range(N):
    Xi, Yi = map(int, stdin.readline().split(' '))

    if