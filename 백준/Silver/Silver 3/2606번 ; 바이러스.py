# https://www.acmicpc.net/problem/2606

from sys import stdin


computer_cnt = int(stdin.readline())
computer_pairs_cnt = int(stdin.readline())
pairs = []

for pair_idx in range(computer_pairs_cnt):
    pairs[pair_idx] = set(stdin.readline().rstrip().split(' '))

