# https://www.acmicpc.net/problem/14916

from sys import stdin

n = int(stdin.readline())
coins = [5, 2]
coins_cnt = 0

for coin in coins:
    coin_cnt = n // coin

    coins_cnt += coin_cnt
    n -= coin_cnt * coin

if n != 0:
    print(-1)
else:
    print(coins_cnt)