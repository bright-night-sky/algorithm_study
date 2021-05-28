# https://www.acmicpc.net/problem/18511

from sys import stdin

N, K = stdin.readline().split(' ')
K = int(K)
elements = sorted(list(map(int, stdin.readline().split(' '))), reverse=True)
result = ''


