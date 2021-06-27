# https://www.acmicpc.net/problem/4383

from sys import stdin


n = list(map(int, stdin.readline().split(' ')))
n_len = len(n)
jolly_jumper = []

for i in range(0, n-1):
    for j in range(i+1, n):
