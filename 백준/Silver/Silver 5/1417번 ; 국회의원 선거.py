# https://www.acmicpc.net/problem/1417

from sys import stdin

N = int(stdin.readline())
candidates = [None] * N

for candidate_idx in range(N):
    candidates[candidate_idx] = int(stdin.readline())

dasom_voted = candidates[0]
all_voted = sum(candidates)

