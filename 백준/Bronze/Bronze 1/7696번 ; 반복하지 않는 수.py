# https://www.acmicpc.net/problem/7696

from sys import stdin

# 0을 입력할 때까지 반복합니다.
while True:
    n = int(stdin.readline().rstrip())

    if n == 0:
        break
    else:
        number = 1
        index = 1
        while True:
            if str(number)