# https://www.acmicpc.net/problem/8979

from sys import stdin

N, K = map(int, stdin.readline().rstrip().split(' '))

nations_medals = []

for nation_idx in range(N):
    nation_medals = list(map(int, stdin.readline().rstrip().split(' ')))
    nations_medals.append(nation_medals[1:])

ranked_nations_medals = sorted(nations_medals, key=lambda nation_medals: (-nation_medals[0], -nation_medals[1], -nation_medals[2]))
print(ranked_nations_medals)
K_rank = ranked_nations_medals.index(nations_medals[K - 1]) + 1

print(K_rank)
