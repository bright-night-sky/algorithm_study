# https://www.acmicpc.net/problem/11947

from sys import stdin


def F(number):
    number = str(number)
    reverse_num = ''

    for position in number:
        reverse_num += str(9 - int(position))

    return int(reverse_num)


T = int(stdin.readline())

for test_case_idx in range(T):
    N = int(stdin.readline())
    max_lovable = 0

    for number in range(1, N + 1):
        Fn = F(number)
        lovable = number * Fn

        if lovable > max_lovable:
            max_lovable = lovable

    print(max_lovable)