# https://www.acmicpc.net/problem/1463

from sys import stdin


N = int(stdin.readline())
operation_cnt = 0

while True:
    if N == 1:
        print(operation_cnt)
        break
    elif N % 3 == 0:
        N //= 3
        operation_cnt += 1
    elif N % 2 == 0:
        N //= 2
        operation_cnt += 1
    else:
        N -= 1
        operation_cnt += 1