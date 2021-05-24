# https://www.acmicpc.net/problem/1236

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split(' '))

current_castle = []


for height_index in range(N):
    current_floor = list(stdin.readline().rstrip())

    current_castle.append(current_floor)


