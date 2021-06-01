# https://www.acmicpc.net/problem/2456

from sys import stdin

N = int(stdin.readline())
candidate1 = [0] * 4
candidate2 = [0] * 4
candidate3 = [0] * 4

for vote_idx in range(N):
    vote = list(map(int, stdin.readline().split(' ')))

    candidate1[0] += vote[0]
    candidate1[vote[0]] += 1

    candidate2[0] += vote[1]
    candidate2[vote[1]] += 1

    candidate3[0] += vote[2]
    candidate3[vote[2]] += 1

