# https://www.acmicpc.net/problem/16428

from sys import stdin


A, B = map(int, stdin.readline().split(' '))

print(A // B)
print(A % B)