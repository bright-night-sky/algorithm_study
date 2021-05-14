# https://www.acmicpc.net/problem/1009

from sys import stdin

T = int(stdin.readline())

for test_case_idx in range(T):
    a, b = map(int, stdin.readline().split(' '))
    one_position = a

    for repeat in range(b - 1):
        one_position = int(str(one_position * a)[-1])

    print(one_position)