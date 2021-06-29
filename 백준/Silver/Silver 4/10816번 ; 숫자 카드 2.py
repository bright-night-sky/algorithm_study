# https://www.acmicpc.net/problem/10816

from sys import stdin


N = int(stdin.readline())
cards = tuple(map(int, stdin.readline().split(' ')))
M = int(stdin.readline())
cnt_cards = tuple(map(int, stdin.readline().split(' ')))

for card in cnt_cards:
    cnt = cards.count(card)

    print(cnt, end=' ')