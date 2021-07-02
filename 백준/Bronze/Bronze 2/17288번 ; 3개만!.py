# https://www.acmicpc.net/problem/17288

from sys import stdin


S = stdin.readline().rstrip()
S_len = len(S)
three_continue = 0

for idx in range(0, S_len - 3, 3):
    if S[idx]