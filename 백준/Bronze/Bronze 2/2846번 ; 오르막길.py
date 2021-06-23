# https://www.acmicpc.net/problem/2846

from sys import stdin


N = int(stdin.readline())
P = list(map(int, stdin.readline().split(' ')))
uphill = []
max_height = 0

for idx in range(1, N):
    if P[idx-1] < P[idx]:
        uphill.append(P[idx])

