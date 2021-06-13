# https://www.acmicpc.net/problem/17262

from sys import stdin


N = int(stdin.readline())
fans_times = [None] * N
max_ei = 0

for fan_idx in range(N):
    fan_time = list(map(int, stdin.readline().split(' ')))

    if fan_time[1] > max_ei:
        max_ei = fan_time[1]

time = [None] * max_ei

for fan_time in fans_times:
    si, ei = fan_time[0], fan_time[1]
    time[si-1:ei] = 1

