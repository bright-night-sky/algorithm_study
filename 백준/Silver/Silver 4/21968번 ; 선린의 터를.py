# https://www.acmicpc.net/problem/21968

from sys import stdin


T = int(stdin.readline())

for site_idx in range(T):
    num = int(stdin.readline())

    print(3 ** (num - 1))