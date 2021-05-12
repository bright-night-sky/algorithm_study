# https://www.acmicpc.net/problem/1312

from sys import stdin

A, B, N = map(int, stdin.readline().rstrip().split(' '))

result = 0
index = 0
while True:
    if index == N:
        print(result)
        break
    else:
