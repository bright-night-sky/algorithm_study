# https://www.acmicpc.net/problem/2303

from sys import stdin
from itertools import combinations

N = int(stdin.readline().rstrip())

people_sum_one = []

for person_idx in range(N):
    cards = list(map(int, stdin.readline().split(' ')))
    cards_combinations = combinations(cards, 3)
    cards_combinations_sum_one = []

    for cards_combination in cards_combinations:
        combination_sum_one = str(sum(cards_combination))[-1]
        cards_combinations_sum_one.append(int(combination_sum_one))

    people_sum_one.append(max(cards_combinations_sum_one))

people_sum_one_max = max(people_sum_one)
people_sum_one_max_idx = people_sum_one.index(people_sum_one_max)

print(people_sum_one_max_idx + 1)