# https://www.acmicpc.net/problem/1620

from sys import stdin

N, M = map(int, stdin.readline().split(' '))
pocketmons = [None] * N

for pocketmon_idx in range(N):
    pocketmons[pocketmon_idx] = stdin.readline().rstrip()

for query_idx in range(M):
    query = stdin.readline().rstrip()

    if ord('0') <= ord(query[0]) <= ord('9'):
        print(pocketmons[int(query) - 1])
    else:
        print(pocketmons.index(query) + 1)