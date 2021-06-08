# https://www.acmicpc.net/problem/12760

from sys import stdin

N, M = map(int, stdin.readline().split(' '))
players_cards = [None] * N

for player_idx in range(N):
    cards = sorted(list(map(int, stdin.readline().split(' '))), reverse=True)

    players_cards[player_idx] = cards

for round_idx in range(M):
    