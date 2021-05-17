# https://www.acmicpc.net/problem/6322

from sys import stdin

test_case_idx = 1

while True:
    a, b, c = map(int, stdin.readline().split(' '))

    if a == b == c == 0:
        break
    else:
        minus_var = None
        is_possible =

        if a == -1:
            if c > b:
                minus_var = 'a'
                a = (c ** 2 - b ** 2) ** 0.5
            else:
