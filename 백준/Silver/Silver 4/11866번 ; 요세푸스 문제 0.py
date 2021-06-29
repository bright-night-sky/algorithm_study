# https://www.acmicpc.net/problem/11866

from sys import stdin


N, K = map(int, stdin.readline().split(' '))
 = []

for _ in range(N):
    if K > N:
        K -= N
        if K in deleted:
            K += 1

    deleted.append(K)

    K += K

print(deleted)