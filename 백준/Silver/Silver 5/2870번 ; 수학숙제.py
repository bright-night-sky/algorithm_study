# https://www.acmicpc.net/problem/2870

from sys import stdin

N = int(stdin.readline())

numbers = []

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for line_idx in range(N):
    line = stdin.readline().rstrip()
    number = line.strip(alphabet)
    print(number)