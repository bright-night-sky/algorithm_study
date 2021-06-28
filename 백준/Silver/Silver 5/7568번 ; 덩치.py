# https://www.acmicpc.net/problem/7568

from sys import stdin


N = int(stdin.readline())
body_infos = [None] * N

for body_idx in range(N):
    body_info = map(int, stdin.readline().split(' '))