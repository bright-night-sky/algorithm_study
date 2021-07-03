# https://www.acmicpc.net/problem/11815

from sys import stdin


N = stdin.readline().rstrip()
Xs = tuple(map(int, stdin.readline().split(' ')))

print(4 ** 0.5)

# for X in Xs:
#     if str(X ** 0.5)[-2:] == '.0':
#         print(1, end=' ')
#     else:
#         print(0, end=' ')