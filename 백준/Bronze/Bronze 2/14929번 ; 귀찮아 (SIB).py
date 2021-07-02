# https://www.acmicpc.net/problem/14929

from sys import stdin


n = int(stdin.readline())
x = tuple(map(int, stdin.readline().split(' ')))
result = 0

for a in range(n-1):
    for b in range(a+1, n):
        result += x[a] * x[b]

print(result)