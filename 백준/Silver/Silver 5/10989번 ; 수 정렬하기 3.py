# https://www.acmicpc.net/problem/10989

from sys import stdin

N = int(stdin.readline())
numbers = [None] * N

for number_idx in range(N):
    numbers[number_idx] = int(stdin.readline())

numbers.sort()

for number in numbers:
    print(number)