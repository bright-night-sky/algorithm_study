# https://www.acmicpc.net/problem/1297

from sys import stdin


diagonal, h_ratio, w_ration = map(int, stdin.readline().split(' '))

print((25 * 25 + 45 * 45) ** 0.5)