# https://www.acmicpc.net/problem/16466

from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split(' ')))
max_Ai = max(A)

for number in range(1, max_Ai + 1):
    if number not in A:
        print(number)
        break
else:
    print(max_Ai + 1)
