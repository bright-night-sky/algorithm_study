# https://www.acmicpc.net/problem/5618

from sys import stdin

n = int(stdin.readline())

numbers = list(map(int, stdin.readline().split(' ')))

min_number = min(numbers)

common_divisor = [number for number in range(1, min_number + 1)]
