# https://www.acmicpc.net/problem/14491

from sys import stdin


T = int(stdin.readline())
nonary = ''

while True:
    if T < 9:
        break

    nonary += str(T % 9)
    T //= 9

print(nonary[::-1])