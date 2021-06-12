# https://www.acmicpc.net/problem/14654

from sys import stdin


N = int(stdin.readline())
ace = list(map(int, stdin.readline().split(' ')))
daniel = list(map(int, stdin.readline().split(' ')))

for round_num in range(N):
    ace_rsp = ace[round_num]
    daniel_rsp = daniel[round_num]

    if