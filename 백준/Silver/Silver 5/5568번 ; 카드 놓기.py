# https://www.acmicpc.net/problem/5568

from sys import stdin
from itertools import combinations


n = int(stdin.readline())
k = int(stdin.readline())
cards = [None] * n
numbers = set()

for card_idx in range(n):
    cards[card_idx] = stdin.readline().rstrip()

numbers = list(combinations(cards, k))
print(numbers)
print(len(numbers))