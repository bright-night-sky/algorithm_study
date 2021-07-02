# https://www.acmicpc.net/problem/15719

from sys import stdin


N = int(stdin.readline())
A = tuple(map(int, stdin.readline().split(' ')))

for num in A:
    if A.count(num) == 2:
        print(num)
        break