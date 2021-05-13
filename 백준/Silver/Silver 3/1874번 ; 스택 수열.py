# https://www.acmicpc.net/problem/1874

from sys import stdin

n = int(stdin.readline())

first_sequence = [num for num in range(1, n + 1)]
sequence_result = []
will_result = []
stack = []

for num in range(n):
    sequence_result.append(int(stdin.readline()))

