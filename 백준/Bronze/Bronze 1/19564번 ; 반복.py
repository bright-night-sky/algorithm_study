# https://www.acmicpc.net/problem/19564

from sys import stdin

S = stdin.readline().rstrip()

L = len(S)

K = 1

for idx in range(1, L):
    if ord(S[idx]) < ord(S[idx-1]):
        K += 1

print(K)