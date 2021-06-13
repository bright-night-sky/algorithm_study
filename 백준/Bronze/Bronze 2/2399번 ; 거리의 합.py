# https://www.acmicpc.net/problem/2399

from sys import stdin


n = int(stdin.readline())
x = list(map(int, stdin.readline().split(' ')))
distance_sum = 0

for idx in range(1, n):
    distance_sum += abs(x[0] - x[idx])

print(distance_sum * (n - 1))