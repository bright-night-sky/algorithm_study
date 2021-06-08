# https://www.acmicpc.net/problem/12971

from sys import stdin

P1, P2, P3, X1, X2, X3 = map(int, stdin.readline().split(' '))
N = max(P1, P2, P3)

for number in range(N, 1000000000):
    if N % P1 == X1 and N % P2 == X2 and N % P3 == X3:
        N = number
        break
else:
    N = -1

print(N)