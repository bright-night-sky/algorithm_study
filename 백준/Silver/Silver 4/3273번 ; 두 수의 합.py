# https://www.acmicpc.net/problem/3273

from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split(' ')))
x = int(stdin.readline())
pair_cnt = 0

for i in range(n - 1):
    ajs = a[i+1:]

    if (x - a[i]) in ajs:
        pair_cnt += 1

print(pair_cnt)