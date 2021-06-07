# https://www.acmicpc.net/problem/20551

from sys import stdin

N, M = map(int, stdin.readline().split(' '))
A = [None] * N

for i in range(N):
    A[i] = int(stdin.readline())

B = sorted(A)

for query_idx in range(M):
    D = int(stdin.readline())

    if D in B:
        print(B.)
    else:
        print(-1)