# https://www.acmicpc.net/problem/2738

from sys import stdin


N, M = map(int, stdin.readline().split(' '))
A = [None] * N
B = [None] * N

for line_idx in range(N):
    A[line_idx] = list(map(int, stdin.readline().split(' ')))

for line_idx in range(N):
    B[line_idx] = list(map(int, stdin.readline().split(' ')))

for line_idx in range(N):
    A.