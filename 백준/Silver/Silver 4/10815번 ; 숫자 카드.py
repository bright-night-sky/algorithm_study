# https://www.acmicpc.net/problem/10815

from sys import stdin

N = stdin.readline()
cards = list(map(int, stdin.readline().split(' ')))
M = stdin.readline()
numbers = list(map(int, stdin.readline().split(' ')))

for number in numbers:
    if number in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')