# https://www.acmicpc.net/problem/20411

from sys import stdin


m, Seed, X1, X2 = map(int, stdin.readline().split(' '))
a, c = 1, 1
ac_founded = False

for a in range(0, m):
    for c in range(0, m):
        if X1 == (a * Seed + c) % m and X2 == (a * X1 + c) % m:
            print(a, c)
            ac_founded = True
            break

    if ac_founded:
        break