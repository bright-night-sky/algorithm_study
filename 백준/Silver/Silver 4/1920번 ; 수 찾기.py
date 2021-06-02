# https://www.acmicpc.net/problem/1920

from sys import stdin

N = int(stdin.readline())
AN = list(map(int, stdin.readline().split(' ')))
M = int(stdin.readline())
M_number = list(map(int, stdin.readline().split(' ')))

for number in M_number:
    if number in AN:
        print(1)
    else:
        print(0)