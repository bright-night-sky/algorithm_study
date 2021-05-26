# https://www.acmicpc.net/problem/2581

from sys import stdin

M = int(stdin.readline())
N = int(stdin.readline())

primes = [2, 3]

for number in range(5, M + 1):
    while True:
