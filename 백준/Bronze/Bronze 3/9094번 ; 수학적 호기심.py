# https://www.acmicpc.net/problem/9094

from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    n, m = map(int, stdin.readline().split(' '))
    ab_cnt = 0

    for a in range(1, n - 1):
        for b in range(a + 1, n):
            equation = (a ** 2 + b ** 2 + m) / (a * b)

            if str(equation)[-2:] == '.0':
                ab_cnt += 1

    print(ab_cnt)