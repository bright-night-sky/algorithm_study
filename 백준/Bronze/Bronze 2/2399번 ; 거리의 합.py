# https://www.acmicpc.net/problem/2399

from sys import stdin


n = int(stdin.readline())
x = list(map(int, stdin.readline().split(' ')))
distance_sum = 0

for xi in x:
    for xj in x:
        distance_sum += abs(xi - xj)

print(distance_sum)