# https://www.acmicpc.net/problem/1312

from sys import stdin

A, B, N = map(int, stdin.readline().split(' '))
float_num = str(A / B)
print(float_num)
float_part = float_num.split('.')[1]

print(float_part[N - 1])